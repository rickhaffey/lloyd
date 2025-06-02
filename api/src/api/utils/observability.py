import logging
from loguru import logger
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

# otel trace imports
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
)
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# otel metrics imports
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
    PeriodicExportingMetricReader,
)
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter

# otel logs imports
from opentelemetry._logs import set_logger_provider
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor


from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor


class PropagateHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        logging.getLogger(record.name).handle(record)


def instrument(app, service_name):
    resource = Resource.create(
        attributes={
            SERVICE_NAME: service_name,
            "service.name": service_name,
            "app_name": service_name,
        }
    )

    # Tracing Setup
    tracer_provider = TracerProvider(resource=resource)
    tracer_provider.add_span_processor(
        BatchSpanProcessor(OTLPSpanExporter(insecure=True))
    )
    trace.set_tracer_provider(tracer_provider)

    # Metrics Setup
    metric_reader = PeriodicExportingMetricReader(OTLPMetricExporter(insecure=True))
    meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])
    metrics.set_meter_provider(meter_provider)

    # Logging Setup
    # create and set the logger provider
    logger_provider = LoggerProvider(resource=resource)
    set_logger_provider(logger_provider)

    # create the OTLP log exporter that sends logs to configured destination
    log_exporter = OTLPLogExporter(insecure=True)
    logger_provider.add_log_record_processor(BatchLogRecordProcessor(log_exporter))

    # attach OTLP handler to root logger
    handler = LoggingHandler(logger_provider=logger_provider)
    logging.getLogger().addHandler(handler)

    # configure loguru to propagate structured logs to standard python logging
    logger.add(PropagateHandler(), serialize=True)

    # instrument logging to automatically inject tracing context into log statements
    LoggingInstrumentor().instrument(set_logging_format=False)

    # instrument FastAPI to automatically emit otel signals
    FastAPIInstrumentor.instrument_app(
        app, tracer_provider=tracer_provider, meter_provider=meter_provider
    )

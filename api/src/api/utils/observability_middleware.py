import time
from typing import Tuple

from opentelemetry.sdk.resources import Resource, SERVICE_NAME

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Match
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from starlette.types import ASGIApp


from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter


class MetricsMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, app_name: str = "fastapi-app") -> None:
        super().__init__(app)
        self.app_name = app_name

        service_name = "app-a"
        resource = Resource.create(
            attributes={
                SERVICE_NAME: service_name,
                "service.name": service_name,
                "app_name": service_name,
            }
        )

        # Metrics Setup
        metric_reader = PeriodicExportingMetricReader(OTLPMetricExporter(insecure=True))
        meter_provider = MeterProvider(
            resource=resource, metric_readers=[metric_reader]
        )
        metrics.set_meter_provider(meter_provider)

        # Creates a meter from the global meter provider
        meter = metrics.get_meter("lloyd.otel.meter")

        self.INFO = meter.create_gauge(
            name="fastapi_app_info", description="FastAPI application information."
        )

        self.REQUESTS = meter.create_counter(
            name="fastapi_requests_total",
            description="Total count of requests by method and path.",
        )

        self.RESPONSES = meter.create_counter(
            name="fastapi_responses_total",
            description="Total count of responses by method, path and status codes.",
        )

        self.REQUESTS_PROCESSING_TIME = meter.create_histogram(
            name="fastapi_requests_duration_seconds",
            description="Histogram of requests processing time by path (in seconds)",
            explicit_bucket_boundaries_advisory=[
                0.005,
                0.01,
                0.025,
                0.05,
                0.075,
                0.1,
                0.25,
                0.5,
                0.75,
                1,
                2.5,
                5,
                7.5,
                10,
            ],
        )

        self.EXCEPTIONS = meter.create_counter(
            name="fastapi_exceptions_total",
            description="Total count of exceptions raised by path and exception type",
        )

        self.REQUESTS_IN_PROGRESS = meter.create_up_down_counter(
            name="fastapi_requests_in_progress",
            description="Gauge of requests by method and path currently being processed",
        )

        self.INFO.set(1, attributes={"app_name": self.app_name})

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        method = request.method
        path, is_handled_path = self.get_path(request)

        if not is_handled_path:
            return await call_next(request)

        # attributes that are common across all instruments
        metric_attributes = {"method": method, "path": path, "app_name": self.app_name}

        self.INFO.set(1, attributes={"app_name": self.app_name})
        self.REQUESTS_IN_PROGRESS.add(1, attributes=metric_attributes)
        self.REQUESTS.add(1, attributes=metric_attributes)
        before_time = time.perf_counter()
        try:
            response = await call_next(request)
        except BaseException as e:
            status_code = HTTP_500_INTERNAL_SERVER_ERROR
            self.EXCEPTIONS.add(
                1, attributes=dict(metric_attributes, exception_type=type(e).__name__)
            )
            raise e from None
        else:
            status_code = response.status_code
            after_time = time.perf_counter()

            # TODO: investigate how to handle this with otel sdk
            # retrieve trace id for exemplar
            # span = trace.get_current_span()
            # trace_id = trace.format_trace_id(span.get_span_context().trace_id)

            self.REQUESTS_PROCESSING_TIME.record(
                after_time - before_time,
                # attributes=dict(metric_attributes, TraceID=trace_id),
                attributes=metric_attributes,
            )
        finally:
            self.RESPONSES.add(
                1, attributes=dict(metric_attributes, status_code=status_code)
            )
            self.REQUESTS_IN_PROGRESS.add(-1, attributes=metric_attributes)

        return response

    @staticmethod
    def get_path(request: Request) -> Tuple[str, bool]:
        for route in request.app.routes:
            match, child_scope = route.matches(request.scope)
            if match == Match.FULL:
                return route.path, True

        return request.url.path, False

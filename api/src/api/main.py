from opentelemetry import metrics
from .utils.observability import instrument
from fastapi import FastAPI
import psycopg
from pydantic import BaseModel
from psycopg.rows import class_row
import os
from loguru import logger
import time
import random

from .routers import observability_demo
from .utils.observability_middleware import MetricsMiddleware

app = FastAPI()

app.add_middleware(MetricsMiddleware, app_name="app-a")

app.include_router(observability_demo.router)

meter = metrics.get_meter("lloyd.otel.meter")

work_counter = meter.create_counter(
    "request.counter", unit="1", description="Counts the number of requests made"
)


class Recipe(BaseModel):
    id: int
    name: str


def get_connection():
    host = os.environ["POSTGRES_SERVER"]
    port = os.environ["POSTGRES_PORT"]
    dbname = os.environ["POSTGRES_DB"]
    user = os.environ["POSTGRES_USER"]
    password = os.environ["POSTGRES_PASSWORD"]

    return psycopg.connect(
        f"host={host} port={port} dbname={dbname} user={user} password={password}"
    )


@app.get("/recipes")
def read_recipes():
    time.sleep(random.randint(5, 10))
    work_counter.add(1, {"work.type": "read_recipe"})
    result = []

    logger.debug("read_recipes: LOG MESSAGE DEMO - DEBUG")
    logger.info("read_recipes: LOG MESSAGE DEMO - INFO")
    logger.warning("read_recipes: LOG MESSAGE DEMO - WARNING")
    logger.error("read_recipes: LOG MESSAGE DEMO - ERROR")
    logger.critical("read_recipes: LOG MESSAGE DEMO - CRITICAL")

    with get_connection() as conn, conn.cursor(row_factory=class_row(Recipe)) as cur:
        cur.execute("SELECT * FROM recipes")
        for record in cur:
            result.append(record)

    return result


instrument(app, service_name="lloyd-api")

from loguru import logger
from fastapi import APIRouter, Response
import random
import time
from typing import Optional
from opentelemetry.propagate import inject
import httpx

# import uvicorn
# from fastapi import FastAPI, Response
# from utils import PrometheusMiddleware, metrics, setting_otlp

TARGET_ONE_HOST = "localhost"
TARGET_TWO_HOST = "localhost"
TARGET_THREE_HOST = "localhost"


router = APIRouter(prefix="/observability_demo", tags=["observability_demo"])


@router.get("/")
async def read_root():
    logger.error("Hello World")
    return {"Hello": "World"}


@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    logger.error("items")
    return {"item_id": item_id, "q": q}


@router.get("/io_task")
async def io_task():
    time.sleep(1)
    logger.error("io task")
    return "IO bound task finish!"


@router.get("/cpu_task")
async def cpu_task():
    for i in range(1000):
        _ = i * i * i
    logger.error("cpu task")
    return "CPU bound task finish!"


@router.get("/random_status")
async def random_status(response: Response):
    response.status_code = random.choice([200, 200, 300, 400, 500])
    logger.error("random status")
    return {"path": "/random_status"}


@router.get("/random_sleep")
async def random_sleep(response: Response):
    time.sleep(random.randint(0, 5))
    logger.error("random sleep")
    return {"path": "/random_sleep"}


@router.get("/error_test")
async def error_test(response: Response):
    logger.error("got error!!!!")
    raise ValueError("value error")


@router.get("/chain")
async def chain(response: Response):
    headers = {}
    inject(headers)  # inject trace info to header
    logger.critical(headers)

    async with httpx.AsyncClient() as client:
        await client.get(
            f"http://{TARGET_ONE_HOST}:8000/",
            headers=headers,
        )
    async with httpx.AsyncClient() as client:
        await client.get(
            f"http://{TARGET_TWO_HOST}:8000/io_task",
            headers=headers,
        )
    async with httpx.AsyncClient() as client:
        await client.get(
            f"http://{TARGET_THREE_HOST}:8000/cpu_task",
            headers=headers,
        )
    logger.info("Chain Finished")
    return {"path": "/chain"}

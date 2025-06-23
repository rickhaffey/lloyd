from .utils.observability import instrument
from fastapi import FastAPI

from .routers import observability_demo
from .routers import recipes
from .utils.observability_middleware import MetricsMiddleware

app = FastAPI()

app.add_middleware(MetricsMiddleware, app_name="app-a")

app.include_router(observability_demo.router)
app.include_router(recipes.router)

instrument(app, service_name="lloyd-api")

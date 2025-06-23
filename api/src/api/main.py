from opentelemetry import metrics
from .utils.observability import instrument
from fastapi import FastAPI

from .routers import observability_demo
from .utils.observability_middleware import MetricsMiddleware
from .models.recipe import Recipe
from .data_access.recipe_repository import RecipeRepository

app = FastAPI()

app.add_middleware(MetricsMiddleware, app_name="app-a")

app.include_router(observability_demo.router)

meter = metrics.get_meter("lloyd.otel.meter")

work_counter = meter.create_counter(
    "request.counter", unit="1", description="Counts the number of requests made"
)

repository = RecipeRepository()


@app.get("/recipes")
def read_recipes() -> list[Recipe]:
    work_counter.add(1, {"work.type": "read_recipe"})
    return repository.get_all_recipes()


instrument(app, service_name="lloyd-api")

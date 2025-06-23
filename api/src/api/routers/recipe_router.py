from fastapi import APIRouter
from opentelemetry import metrics
from ..models.recipe import Recipe
from ..data_access.recipe_repository import RecipeRepository


router = APIRouter(prefix="/recipes", tags=["recipes"])

meter = metrics.get_meter("lloyd.otel.meter")

work_counter = meter.create_counter(
    "request.counter", unit="1", description="Counts the number of requests made"
)

repository = RecipeRepository()


@router.get("/")
def read_recipes() -> list[Recipe]:
    work_counter.add(1, {"work.type": "read_recipe"})
    return repository.get_all_recipes()

from fastapi import APIRouter

from model.recipe_request import RecipeRequest
from model.recipe_response import RecipeResponse
from service.receipt_generator_service import get_recipe

recipe_router = APIRouter(prefix="/receipt")


@recipe_router.post("/")
async def generate_recipe(request: RecipeRequest) -> RecipeResponse:
    result = await get_recipe(request)
    return result

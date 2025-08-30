import json

from model.recipe_request import RecipeRequest
from service.recipe_service import RecipeService
from langchain_core.messages import BaseMessage



async def get_recipe(recipe_request: RecipeRequest):
    """Generate a recipe based on the provided ingredients and context."""
    ai_message: BaseMessage = RecipeService().get_recipe(recipe_request)
    return json.loads(ai_message.content)


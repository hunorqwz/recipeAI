from pydantic import BaseModel


class RecipeResponse(BaseModel):
    """
    Pydantic model for the response of a receipt.
    """
    title: str
    description: str
    ingredients: list[str]
    instructions: list[str]
    tips: list[str]

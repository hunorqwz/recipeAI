from enum import Enum
from pydantic import BaseModel

class ReceiptType(Enum):
    VEGAN = "vegan"
    OMNIVORE = "omnivore"
    VEGETARIAN = "vegetarian"
    CETO = "ceto"


class DifficultyLevel(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class CuisineType(Enum):
    ITALIAN = "italian"
    MEXICAN = "mexican"
    ASIAN = "asian"


class DietaryRestriction(Enum):
    GLUTEN_FREE = "gluten_free"
    DAIRY_FREE = "dairy_free"
    KOSHER = "kosher"
    HALAL = "halal"


class RecipeRequest(BaseModel):
    type: ReceiptType = ReceiptType.OMNIVORE
    ingridients: list[str]
    # cooking_time_minutes: int
    # difficulty_level: DifficultyLevel
    # cuisine_type: CuisineType
    # dietary_restrictions: list[DietaryRestriction]
    # equipment_needed: list[str]

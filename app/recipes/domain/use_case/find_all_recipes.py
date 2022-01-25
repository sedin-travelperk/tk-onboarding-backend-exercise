from typing import List

from recipes.domain.entity.recipe import Recipe
from recipes.domain.interface.recipe_service import RecipeService


class FindAllRecipesUseCase:

    def __init__(self, recipe_service: RecipeService):
        self.recipe_service = recipe_service

    def execute(self) -> List[Recipe]:
        return self.recipe_service.find_all()

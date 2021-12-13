from typing import List

from recipes.domain.exceptions import RecipeNotFound, DataNotFound
from recipes.domain.recipe import Recipe
from recipes.ports.recipe_repository import RecipeRepository
from recipes.ports.recipe_service import RecipeService


class RecipeServiceImpl(RecipeService):
    """Implementation for recipe service"""

    def __init__(self, repository: RecipeRepository):
        self.repository = repository

    def get(self, recipe_id: int) -> Recipe:
        try:
            return self.repository.get(recipe_id=recipe_id)
        except DataNotFound as e:
            print(e)
            raise RecipeNotFound(f'Recipe with id -> {recipe_id} not found!')

    def find_all(self) -> List[Recipe]:
        return self.repository.find_all()

    def create(self, data: dict) -> Recipe:
        recipe = Recipe(**data)

        return self.repository.create(recipe=recipe)

    def update(self, recipe_id: int, data: dict) -> Recipe:
        recipe = self.get(recipe_id=recipe_id)

        recipe.update(**data)

        self.repository.update(recipe=recipe)

        return self.get(recipe_id=recipe_id)

    def delete(self, recipe_id: int) -> None:
        self.get(recipe_id=recipe_id)

        self.repository.delete(recipe_id=recipe_id)



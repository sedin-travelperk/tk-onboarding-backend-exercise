from recipes.domain.entity.recipe import Recipe
from recipes.domain.exceptions.data_not_found import DataNotFound
from recipes.domain.exceptions.recipe_not_found import RecipeNotFound
from recipes.domain.interface.recipe_service import RecipeService


class GetRecipe:

    def __init__(self, recipe_service: RecipeService):
        self.recipe_service = recipe_service

    def execute(self, id: int) -> Recipe:
        try:
            return self.recipe_service.get(recipe_id=id)
        except DataNotFound as e:
            raise RecipeNotFound(f'Recipe with id -> {id} not found!')


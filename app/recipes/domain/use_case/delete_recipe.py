from recipes.domain.exceptions.data_not_found import DataNotFound
from recipes.domain.exceptions.recipe_not_found import RecipeNotFound
from recipes.domain.interface.recipe_service import RecipeService


class DeleteRecipe:
    def __init__(self, recipe_service: RecipeService):
        self.recipe_service = recipe_service

    def execute(self, recipe_id: int) -> None:
        try:
            self.recipe_service.delete(recipe_id=recipe_id)
        except DataNotFound as e:
            raise RecipeNotFound(f'Recipe with id -> {id} not found!')

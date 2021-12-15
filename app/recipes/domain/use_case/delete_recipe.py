from recipes.domain.exceptions.recipe_not_found import RecipeNotFound
from recipes.domain.interface.recipe_service import RecipeService


class DeleteRecipe:
    def __init__(self, recipe_service: RecipeService):
        self.recipe_service = recipe_service

    def execute(self, recipe_id: int) -> None:
        if not self.recipe_service.exists(recipe_id=recipe_id):
            raise RecipeNotFound(recipe_id=recipe_id)

        self.recipe_service.delete(recipe_id=recipe_id)


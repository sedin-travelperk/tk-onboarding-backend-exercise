from recipes.domain.entity.recipe import Recipe
from recipes.domain.exceptions.recipe_not_found import RecipeNotFound
from recipes.domain.interface.recipe_service import RecipeService


class GetRecipe:

    def __init__(self, recipe_service: RecipeService):
        self.recipe_service = recipe_service

    def execute(self, recipe_id: int) -> Recipe:
        if not self.recipe_service.exists(recipe_id=recipe_id):
            raise RecipeNotFound(recipe_id=recipe_id)

        return self.recipe_service.get(recipe_id=recipe_id)



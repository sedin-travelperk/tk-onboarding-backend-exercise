from recipes.domain.entity.recipe import Recipe
from recipes.domain.interface.recipe_service import RecipeService


class CreateRecipe:

    def __init__(self, recipe_service: RecipeService):
        self.recipe_service = recipe_service

    def execute(self, recipe: Recipe) -> Recipe:
        return self.recipe_service.create(recipe=recipe)

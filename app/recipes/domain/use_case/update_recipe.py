from recipes.domain.entity.ingredient import Ingredient
from recipes.domain.entity.recipe import Recipe
from recipes.domain.exceptions.recipe_not_found import RecipeNotFound
from recipes.domain.interface.recipe_service import RecipeService


class UpdateRecipe:

    def __init__(self, recipe_service: RecipeService):
        self.recipe_service = recipe_service

    def _update_recipe(self, recipe_id: int, data: dict) -> Recipe:
        name = data.get('name')
        description = data.get('description')
        new_ingredients = data.get('ingredients', None)

        recipe = self.recipe_service.get(recipe_id=recipe_id)

        if name:
            recipe.name = name

        if description:
            recipe.description = description

        if new_ingredients:
            recipe.ingredients = [Ingredient(name=ingredient['name']) for ingredient in new_ingredients]
        else:
            recipe.ingredients = []

        return recipe

    def execute(self, recipe_id: int, data: dict) -> Recipe:
        if not self.recipe_service.exists(recipe_id=recipe_id):
            raise RecipeNotFound(recipe_id=recipe_id)

        recipe = self._update_recipe(recipe_id=recipe_id, data=data)

        return self.recipe_service.update(recipe=recipe)






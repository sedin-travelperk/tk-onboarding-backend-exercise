from typing import List

from recipes.domain.interface.recipe_repository import RecipeRepository
from recipes.domain.interface.recipe_service import RecipeService
from recipes.adapters.repository.ingredient_repository_impl import IngredientRepositoryImpl
from recipes.domain.entity.ingredient import Ingredient
from recipes.domain.entity.recipe import Recipe


class RecipeServiceImpl(RecipeService):
    """Implementation for recipe service"""

    def __init__(self, recipe_repository: RecipeRepository, ingredient_repository: IngredientRepositoryImpl):
        self.recipe_repository = recipe_repository
        self.ingredient_repository = ingredient_repository

    def get(self, recipe_id: int) -> Recipe:
        recipe = self.recipe_repository.get(recipe_id=recipe_id)
        recipe.ingredients = self.ingredient_repository.find_by_recipe_id(recipe_id=recipe_id)

        return recipe

    def find_all(self) -> List[Recipe]:
        recipes = self.recipe_repository.find_all()

        for recipe in recipes:
            recipe.ingredients = self.ingredient_repository.find_by_recipe_id(recipe_id=recipe.recipe_id)

        return recipes

    def find_by_name(self, name: str) -> List[Recipe]:
        recipes = self.recipe_repository.find_by_name(name=name)

        for recipe in recipes:
            recipe.ingredients = self.ingredient_repository.find_by_recipe_id(recipe_id=recipe.recipe_id)

        return recipes

    def create(self, recipe: Recipe) -> Recipe:
        new_recipe = self.recipe_repository.create(recipe=recipe)

        for ingredient in recipe.ingredients:
            new_ingredient = Ingredient(
                name=ingredient.name
            )
            new_recipe.ingredients.append(self.ingredient_repository.create(new_ingredient, new_recipe.recipe_id))

        return new_recipe

    def update(self, recipe: Recipe) -> Recipe:
        self.recipe_repository.update(recipe=recipe)

        if recipe.ingredients:
            self.ingredient_repository.delete_by_recipe(recipe_id=recipe.recipe_id)

            for ingredient in recipe.ingredients:
                self.ingredient_repository.create(ingredient=ingredient, recipe_id=recipe.recipe_id)

        return self.get(recipe_id=recipe.recipe_id)

    def delete(self, recipe_id: int) -> None:
        self.recipe_repository.delete(recipe_id=recipe_id)

    def exists(self, recipe_id: int) -> bool:
        return self.recipe_repository.exists(recipe_id=recipe_id)



import json
from typing import List

from recipes.adapters.ingredient_repository_impl import IngredientRepositoryImpl
from recipes.domain.exceptions import RecipeNotFound, DataNotFound
from recipes.domain.ingredient import Ingredient
from recipes.domain.recipe import Recipe
from recipes.ports.recipe_repository import RecipeRepository
from recipes.ports.recipe_service import RecipeService


class RecipeServiceImpl(RecipeService):
    """Implementation for recipe service"""

    def __init__(self, repository: RecipeRepository, ingredient_repository: IngredientRepositoryImpl):
        self.recipe_repository = repository
        self.ingredient_repository = ingredient_repository

    def get(self, recipe_id: int) -> Recipe:
        try:
            return self.recipe_repository.get(recipe_id=recipe_id)
        except DataNotFound as e:
            print(e)
            raise RecipeNotFound(f'Recipe with id -> {recipe_id} not found!')

    def find_all(self) -> List[Recipe]:
        recipes = self.recipe_repository.find_all()

        for recipe in recipes:
            recipe.ingredients = self.ingredient_repository.find_by_recipe_id(recipe_id=recipe.recipe_id)

        return recipes

    def create(self, data: dict) -> Recipe:
        recipe = Recipe(
            name=data['name'],
            description=data['description']
        )

        new_recipe = self.recipe_repository.create(recipe=recipe)

        for ingredient in data.get('ingredients', []):
            new_ingredient = Ingredient(
                name=ingredient['name']
            )
            new_recipe.ingredients.append(self.ingredient_repository.create(new_ingredient, new_recipe.recipe_id))

        return new_recipe

    def update(self, recipe_id: int, data: dict) -> Recipe:
        recipe = self.get(recipe_id=recipe_id)

        recipe.update(**data)

        self.recipe_repository.update(recipe=recipe)

        return self.get(recipe_id=recipe_id)

    def delete(self, recipe_id: int) -> None:
        self.get(recipe_id=recipe_id)

        self.recipe_repository.delete(recipe_id=recipe_id)



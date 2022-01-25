from django.db import models

from recipes.domain.entity.ingredient import Ingredient
from recipes.adapters.repository.recipe_orm import RecipeORM


class IngredientORM(models.Model):
    name = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        RecipeORM,
        on_delete=models.CASCADE
    )

    def to_domain_model(self) -> Ingredient:
        return Ingredient(
            ingredient_id=self.id,
            name=self.name
        )

    @staticmethod
    def create_from_domain_model(ingredient: Ingredient, recipe_id: int):
        ingredient_orm = IngredientORM(
            name=ingredient.name
        )
        ingredient_orm.recipe_id = recipe_id

        return ingredient_orm

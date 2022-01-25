from typing import List

from recipes.domain.entity.ingredient import Ingredient
from recipes.domain.interface.ingredients_repository import IngredientRepository

from recipes.adapters.repository.ingredient_orm import IngredientORM


class IngredientRepositoryImpl(IngredientRepository):

    def find_by_recipe_id(self, recipe_id: int) -> List[Ingredient]:
        ingredients: IngredientORM = IngredientORM.objects.filter(recipe=recipe_id)

        return [ingredient.to_domain_model() for ingredient in ingredients]

    def create(self, ingredient: Ingredient, recipe_id: int) -> Ingredient:
        ingredient_orm = IngredientORM.create_from_domain_model(
            ingredient=ingredient,
            recipe_id=recipe_id
        )

        ingredient_orm.save()

        return ingredient_orm.to_domain_model()

    def delete_by_recipe(self, recipe_id: int) -> None:
        IngredientORM.objects.filter(recipe_id=recipe_id).delete()


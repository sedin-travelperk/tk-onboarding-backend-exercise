from typing import List

from recipes.domain.ingredient import Ingredient
from recipes.models import IngredientORM
from recipes.ports.ingredients_repository import IngredientRepository


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

    def delete(self, ingredient_id: int) -> None:
        IngredientORM.objects.filter(id=ingredient_id).delete()

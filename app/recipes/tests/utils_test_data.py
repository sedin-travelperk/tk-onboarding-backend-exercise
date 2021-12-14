from typing import List

from faker import Faker

from recipes.models import RecipeORM, IngredientORM

fake = Faker()


class UtilsTestData:
    """Helper class to generate test data in db"""

    @staticmethod
    def create_and_return_recipe() -> RecipeORM:
        return RecipeORM.objects.create(
            name=fake.name(),
            description=fake.text()
        )

    @staticmethod
    def add_ingredient_to_recipe(recipe: RecipeORM) -> IngredientORM:
        return IngredientORM.objects.create(
            recipe=recipe,
            name=fake.name()
        )

    @staticmethod
    def create_and_return_recipe_with_ingredients() -> RecipeORM:
        recipe = UtilsTestData.create_and_return_recipe()

        UtilsTestData.add_ingredient_to_recipe(recipe=recipe)
        UtilsTestData.add_ingredient_to_recipe(recipe=recipe)

        recipe.save()
        recipe.refresh_from_db()

        return recipe

    @staticmethod
    def get_ingredients_from_db(recipe_id: int) -> List[IngredientORM]:
        return IngredientORM.objects.filter(recipe_id=recipe_id)

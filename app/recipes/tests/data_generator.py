from faker import Faker

from recipes.models import RecipeORM

fake = Faker()


class DataGenerator:
    """Helper class to generate test data in db"""

    @staticmethod
    def create_and_return_recipe_object():
        return RecipeORM.objects.create(
            name=fake.name(),
            description=fake.text()
        )

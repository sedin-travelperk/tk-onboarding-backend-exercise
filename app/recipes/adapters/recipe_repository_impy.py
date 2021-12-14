from typing import List

from recipes.domain.exceptions import DataNotFound
from recipes.domain.recipe import Recipe
from recipes.models import RecipeORM
from recipes.ports.recipe_repository import RecipeRepository


class RecipeRepositoryImpl(RecipeRepository):
    """Implementation for Recipe repository"""

    def get(self, recipe_id: int) -> Recipe:
        try:
            recipe: RecipeORM = RecipeORM.objects.get(id=recipe_id)
            return recipe.to_domain_model()

        except RecipeORM.DoesNotExist as e:
            raise DataNotFound(f'Item with id {recipe_id} not present in db.')

    def find_all(self) -> List[Recipe]:
        recipes = RecipeORM.objects.all()

        return [recipe.to_domain_model() for recipe in recipes]

    def create(self, recipe: Recipe) -> Recipe:
        recipe_orm = RecipeORM.create_from_domain_model(
            name=recipe.name,
            description=recipe.description
        )
        recipe_orm.save()
        recipe_orm.refresh_from_db()

        return recipe_orm.to_domain_model()

    def update(self, recipe: Recipe) -> Recipe:
        recipe_id = RecipeORM.objects.filter(id=recipe.recipe_id).update(
            name=recipe.name,
            description=recipe.description
        )

        return recipe_id

    def delete(self, recipe_id: int) -> None:
        RecipeORM.objects.filter(id=recipe_id).delete()



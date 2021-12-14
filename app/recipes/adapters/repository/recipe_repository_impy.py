from typing import List


from recipes.domain.entity.recipe import Recipe
from recipes.domain.exceptions.data_not_found import DataNotFound
from recipes.domain.interface.recipe_repository import RecipeRepository
from recipes.adapters.repository.recipe_orm import RecipeORM


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

    def find_by_name(self, name: str) -> List[Recipe]:
        recipes = RecipeORM.objects.filter(name__startswith=name)

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




from django.db import models

from recipes.domain.entity.recipe import Recipe


class RecipeORM(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def to_domain_model(self) -> Recipe:
        return Recipe(
            recipe_id=self.id,
            name=self.name,
            description=self.description,
        )

    @staticmethod
    def create_from_domain_model(name, description):
        return RecipeORM(
            name=name,
            description=description
        )

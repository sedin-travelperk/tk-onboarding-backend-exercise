from django.contrib import admin

from recipes.adapters.repository.ingredient_orm import IngredientORM
from recipes.adapters.repository.recipe_orm import RecipeORM

admin.site.register(RecipeORM)
admin.site.register(IngredientORM)

from django.urls import path

from recipes.adapters.views.recipe_details_view import RecipeDetailView
from recipes.adapters.views.recipes_view import RecipesView

urlpatterns = [
    path('', RecipesView.as_view(), name='recipes'),
    path('<int:pk>', RecipeDetailView.as_view(), name='recipes')
]

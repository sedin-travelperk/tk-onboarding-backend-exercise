from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.RecipesView.as_view(), name='recipes'),
    path('<int:pk>', views.RecipeDetailView.as_view(), name='recipes')
]

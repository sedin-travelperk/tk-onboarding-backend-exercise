import json

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from recipes.adapters.ingredient_repository_impl import IngredientRepositoryImpl
from recipes.adapters.recipe_repository_impy import RecipeRepositoryImpl
from recipes.adapters.recipe_service_impl import RecipeServiceImpl
from recipes.domain.recipe import Recipe


class RecipesView(APIView):
    """
    Return list of all recipes or create new one.
    """

    def get(self, request, format=None):
        service = RecipeServiceImpl(repository=RecipeRepositoryImpl(), ingredient_repository=IngredientRepositoryImpl())

        recipes = service.find_all()

        result = [recipe.to_json() for recipe in recipes]

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        service = RecipeServiceImpl(repository=RecipeRepositoryImpl(), ingredient_repository=IngredientRepositoryImpl())

        result = service.create(request.data.dict())

        return Response(result.to_json(), status=status.HTTP_200_OK)


class RecipeDetailView(APIView):
    """
    Retrieve, update or delete a recipe.
    """

    def get(self, request, pk, format=None):
        service = RecipeServiceImpl(repository=RecipeRepositoryImpl(), ingredient_repository=IngredientRepositoryImpl())

        result = service.get(recipe_id=pk)

        return Response(result, status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        service = RecipeServiceImpl(repository=RecipeRepositoryImpl(), ingredient_repository=IngredientRepositoryImpl())

        data = {
            'name': request.data.get('name', None),
            'description': request.data.get('description', None)
        }

        result = service.update(
            recipe_id=pk,
            data=data
        )

        return Response(result.to_json(), status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        service = RecipeServiceImpl(repository=RecipeRepositoryImpl(), ingredient_repository=IngredientRepositoryImpl())

        service.delete(
            recipe_id=pk
        )

        return Response(status=status.HTTP_204_NO_CONTENT)






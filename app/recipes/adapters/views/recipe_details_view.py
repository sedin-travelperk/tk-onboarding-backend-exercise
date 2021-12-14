from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from recipes.adapters.repository.ingredient_repository_impl import IngredientRepositoryImpl
from recipes.adapters.repository.recipe_repository_impy import RecipeRepositoryImpl
from recipes.adapters.services.recipe_service_impl import RecipeServiceImpl


class RecipeDetailView(APIView):
    """
    Retrieve, update or delete a recipe.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.recipe_service = RecipeServiceImpl(
            recipe_repository=RecipeRepositoryImpl(),
            ingredient_repository=IngredientRepositoryImpl()
        )

    def get(self, request, pk, format=None):
        result = self.recipe_service.get(recipe_id=pk)

        return Response(result, status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        result = self.recipe_service.update(
            recipe_id=pk,
            data=request.data
        )

        return Response(result.to_json(), status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        self.recipe_service.delete(
            recipe_id=pk
        )

        return Response(status=status.HTTP_204_NO_CONTENT)






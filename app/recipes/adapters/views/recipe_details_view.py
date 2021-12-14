from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from recipes.adapters.repository.ingredient_repository_impl import IngredientRepositoryImpl
from recipes.adapters.repository.recipe_repository_impy import RecipeRepositoryImpl
from recipes.domain.use_case.recipe_service_impl import RecipeServiceImpl


class RecipeDetailView(APIView):
    """
    Retrieve, update or delete a recipe.
    """

    def get(self, request, pk, format=None):
        service = RecipeServiceImpl(
            recipe_repository=RecipeRepositoryImpl(),
            ingredient_repository=IngredientRepositoryImpl()
        )

        result = service.get(recipe_id=pk)

        return Response(result, status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        service = RecipeServiceImpl(
            recipe_repository=RecipeRepositoryImpl(),
            ingredient_repository=IngredientRepositoryImpl()
        )

        result = service.update(
            recipe_id=pk,
            data=request.data
        )

        return Response(result.to_json(), status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        service = RecipeServiceImpl(
            recipe_repository=RecipeRepositoryImpl(),
            ingredient_repository=IngredientRepositoryImpl()
        )

        service.delete(
            recipe_id=pk
        )

        return Response(status=status.HTTP_204_NO_CONTENT)






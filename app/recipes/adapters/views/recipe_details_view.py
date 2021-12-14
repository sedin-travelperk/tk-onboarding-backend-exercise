from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from recipes.adapters.repository.ingredient_repository_impl import IngredientRepositoryImpl
from recipes.adapters.repository.recipe_repository_impy import RecipeRepositoryImpl
from recipes.adapters.services.recipe_service_impl import RecipeServiceImpl
from recipes.domain.use_case.delete_recipe import DeleteRecipe
from recipes.domain.use_case.get_recipe import GetRecipe
from recipes.domain.use_case.update_recipe import UpdateRecipe


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

    def get(self, request, pk):
        result = GetRecipe(recipe_service=self.recipe_service).execute(id=pk)

        return Response(result.to_json(), status=status.HTTP_200_OK)

    def patch(self, request, pk):
        result = UpdateRecipe(recipe_service=self.recipe_service).execute(
            recipe_id=pk,
            data=request.data
        )

        return Response(result.to_json(), status=status.HTTP_200_OK)

    def delete(self, request, pk):
        DeleteRecipe(recipe_service=self.recipe_service).execute(recipe_id=pk)

        return Response(status=status.HTTP_204_NO_CONTENT)






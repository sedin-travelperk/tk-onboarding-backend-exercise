from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from recipes.adapters.repository.ingredient_repository_impl import IngredientRepositoryImpl
from recipes.adapters.repository.recipe_repository_impy import RecipeRepositoryImpl
from recipes.domain.use_case.recipe_service_impl import RecipeServiceImpl


class RecipesView(APIView):
    """
    Return list of all recipes or create new one.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.recipe_service = RecipeServiceImpl(
            recipe_repository=RecipeRepositoryImpl(),
            ingredient_repository=IngredientRepositoryImpl()
        )

    def get(self, request, format=None):
        recipes = self.recipe_service.find_all()

        result = [recipe.to_json() for recipe in recipes]

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        result = self.recipe_service.create(request.data)

        return Response(result.to_json(), status=status.HTTP_200_OK)






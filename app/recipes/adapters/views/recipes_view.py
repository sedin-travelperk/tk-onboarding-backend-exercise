from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from recipes.adapters.repository.ingredient_repository_impl import IngredientRepositoryImpl
from recipes.adapters.repository.recipe_repository_impy import RecipeRepositoryImpl
from recipes.adapters.services.recipe_service_impl import RecipeServiceImpl
from recipes.domain.entity.ingredient import Ingredient
from recipes.domain.entity.recipe import Recipe
from recipes.domain.use_case.create_recipe import CreateRecipe
from recipes.domain.use_case.find_all_recipes import FindAllRecipesUseCase
from recipes.domain.use_case.find_recipe_by_name import FindRecipesByName


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

    def get(self, request):
        name = request.query_params.get('name')

        if name:
            recipes = FindRecipesByName(recipe_service=self.recipe_service).execute(name=name)
        else:
            recipes = FindAllRecipesUseCase(recipe_service=self.recipe_service).execute()

        result = [recipe.to_json() for recipe in recipes]

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        recipe = Recipe(
            name=data['name'],
            description=data['description']
        )

        for ingredient in data.get('ingredients', []):
            new_ingredient = Ingredient(
                name=ingredient['name']
            )
            recipe.ingredients.append(new_ingredient)

        result = CreateRecipe(recipe_service=self.recipe_service).execute(recipe=recipe)

        return Response(result.to_json(), status=status.HTTP_200_OK)






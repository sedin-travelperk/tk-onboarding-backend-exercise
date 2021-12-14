import json

from django.urls import reverse
from django.test import TestCase

from rest_framework.test import APIClient

from recipes.tests.utils_test_data import UtilsTestData

RECIPE_URL = reverse('recipes')

API_CLIENT_JSON_FORMAT = 'json'


class RecipeTestCase(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.recipe = UtilsTestData.create_and_return_recipe()
        self.recipe_with_ingredients = UtilsTestData.create_and_return_recipe_with_ingredients()

    def get_recipe_url(self) -> str:
        return reverse('recipes')

    def get_recipe_detail_url(self, recipe_id: int) -> str:
        return reverse('recipes', args=[recipe_id])

    def get_json(self, data):
        return json.loads(data)

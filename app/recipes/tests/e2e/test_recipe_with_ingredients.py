import json

from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from recipes.tests.utils_test_data import UtilsTestData

RECIPE_URL = reverse('recipes')

API_CLIENT_JSON_FORMAT = 'json'


def recipe_detail_url(recipe_id: int) -> str:
    return reverse('recipes',  args=[recipe_id])


class RecipeWithIngredientsAPITest(TestCase):
    """Test recipe with ingredients API"""

    def setUp(self) -> None:
        self.client = APIClient()
        self.recipe = UtilsTestData.create_and_return_recipe_with_ingredients()

    def test_retrieve_recipe_list(self):
        """Retrieve recipe with ingredients list from db successful"""

        response = self.client.get(RECIPE_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data_json = json.loads(response.data[0])

        self.assertEqual(response_data_json['name'], self.recipe.name)
        self.assertEqual(response_data_json['description'], self.recipe.description)
        self.assertEqual(len(response_data_json['ingredients']), 2)

    def test_create_recipe_with_ingredients(self):
        """Create recipe with ingredients in db successful"""
        payload = {
            'name': 'Test',
            'description': 'Test description',
            'ingredients': [
                {
                    'name': 'Ingredient one',
                },
                {
                    'name': 'Ingredient two',
                }
            ]
        }

        response = self.client.post(RECIPE_URL, payload, format=API_CLIENT_JSON_FORMAT)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data_json = json.loads(response.data)

        self.assertEqual(response_data_json['name'], payload['name'])
        self.assertEqual(response_data_json['description'], payload['description'])

        response_data_ingredients = response_data_json['ingredients']

        self.assertEqual(len(response_data_ingredients), len(payload['ingredients']))
        self.assertEqual(response_data_ingredients[0]['name'], payload['ingredients'][0]['name'])
        self.assertEqual(response_data_ingredients[1]['name'], payload['ingredients'][1]['name'])

    def test_update_recipe_name(self):
        """Update recipe description for recipe with ingredients is in db successful"""
        payload = {
            'description': 'New description'
        }

        url = recipe_detail_url(recipe_id=self.recipe.id)
        response = self.client.patch(url, payload, format=API_CLIENT_JSON_FORMAT)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data_json = json.loads(response.data)

        self.assertEqual(response_data_json['name'], self.recipe.name)
        self.assertEqual(response_data_json['description'], payload['description'])
        self.assertEqual(len(response_data_json['ingredients']), 2)
        
    def test_update_recipe_ingredient(self):
        """Update recipe ingredient for recipe with ingredient in db successful"""
        payload = {
            'ingredients': [
                {
                    'name': 'New ingredient'
                }
            ]
        }
        
        url = recipe_detail_url(recipe_id=self.recipe.id)
        response = self.client.patch(url, payload, format=API_CLIENT_JSON_FORMAT)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data_json = json.loads(response.data)

        self.assertEqual(response_data_json['name'], self.recipe.name)
        self.assertEqual(response_data_json['description'], self.recipe.description)

        responser_data_ingredients = response_data_json['ingredients']
        self.assertEqual(len(responser_data_ingredients), 1)
        self.assertEqual(responser_data_ingredients[0]['name'], payload['ingredients'][0]['name'])

    def test_delete_recipe_with_ingredients(self):
        """Deleting recipe with ingredients in db successful"""
        url = recipe_detail_url(recipe_id=self.recipe.id)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        ingredients_in_db = UtilsTestData.get_ingredients_from_db(recipe_id=self.recipe.id)

        self.assertEqual(len(ingredients_in_db), 0)

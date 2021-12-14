import json

from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from recipes.tests.data_generator import DataGenerator

RECIPE_URL = reverse('recipes')


def recipe_detail_url(recipe_id: int) -> str:
    return reverse('recipes',  args=[recipe_id])


class RecipeWithIngredientsAPITest(TestCase):
    """Test recipe with ingredients API"""

    def setUp(self) -> None:
        self.client = APIClient()
        self.recipe = DataGenerator.create_and_return_recipe_with_ingredients()

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

        response = self.client.post(RECIPE_URL, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data_json = json.loads(response.data)

        self.assertEqual(response_data_json['name'], payload['name'])
        self.assertEqual(response_data_json['description'], payload['description'])

        response_data_ingredients = response_data_json['ingredients']

        self.assertEqual(len(response_data_ingredients), len(payload['ingredients']))
        self.assertEqual(response_data_ingredients[0]['name'], payload['ingredients'][0]['name'])
        self.assertEqual(response_data_ingredients[1]['name'], payload['ingredients'][1]['name'])

    def test_update_recipe_name(self):
        """Update recipe description for recipe with ingredients that is in db successful"""
        payload = {
            'description': 'New description'
        }

        url = recipe_detail_url(recipe_id=self.recipe.id)
        response = self.client.patch(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data_json = json.loads(response.data)

        self.assertEqual(response_data_json['name'], self.recipe.name)
        self.assertEqual(response_data_json['description'], payload['description'])
        self.assertEqual(len(response_data_json['ingredients']), 2)

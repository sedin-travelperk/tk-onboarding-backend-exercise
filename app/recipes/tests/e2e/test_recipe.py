import json

from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from recipes.tests.data_generator import DataGenerator

RECIPE_URL = reverse('recipes')


def recipe_detail_url(recipe_id: int) -> str:
    return reverse('recipes',  args=[recipe_id])


class RecipeApiTests(TestCase):
    """Test recipe API"""

    def setUp(self) -> None:
        self.client = APIClient()
        self.recipe = DataGenerator.create_and_return_recipe()

    def test_retrieve_recipe_list(self):
        """Retrieve recipe list from db successful"""

        response = self.client.get(RECIPE_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data_json = json.loads(response.data[0])

        self.assertEqual(response_data_json['name'], self.recipe.name)
        self.assertEqual(response_data_json['description'], self.recipe.description)

    def test_create_recipe(self):
        """Creating recipe in db successful"""
        payload = {
            'name': 'Test recipe',
            'description': 'Test description',
        }

        response = self.client.post(RECIPE_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data_json = json.loads(response.data)

        self.assertEqual(response_data_json['name'], payload['name'])
        self.assertEqual(response_data_json['description'], payload['description'])

    def test_update_recipe(self):
        """Updating recipe in db successful"""
        payload = {
            'name': 'New name'
        }

        url = recipe_detail_url(recipe_id=self.recipe.id)
        response = self.client.patch(url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data_json = json.loads(response.data)

        self.assertEqual(response_data_json['name'], payload['name'])
        self.assertEqual(response_data_json['description'], self.recipe.description)

    def test_delete_recipe(self):
        """Deleting recipe from db"""
        url = recipe_detail_url(recipe_id=self.recipe.id)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

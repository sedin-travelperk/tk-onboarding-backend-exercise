from rest_framework import status

from recipes.tests.e2e.recipe_test_case import RecipeTestCase, API_CLIENT_JSON_FORMAT
from recipes.tests.utils_test_data import UtilsTestData


class RecipeWithIngredientsAPITest(RecipeTestCase):
    """Test recipe with ingredients API"""

    def test_retrieve_recipe_with_ingredients(self):
        """Retrieve recipe with ingredients from db"""
        response = self.client.get(
            path=self.get_recipe_detail_url(recipe_id=self.recipe_with_ingredients.id)
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data_json = self.get_json(response.data)

        self.assertEqual(response_data_json['name'], self.recipe_with_ingredients.name)
        self.assertEqual(response_data_json['description'], self.recipe_with_ingredients.description)
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

        response = self.client.post(
            path=self.get_recipe_url(),
            data=payload,
            format=API_CLIENT_JSON_FORMAT
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data_json = self.get_json(response.data)

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

        response = self.client.patch(
            path=self.get_recipe_detail_url(recipe_id=self.recipe_with_ingredients.id),
            data=payload,
            format=API_CLIENT_JSON_FORMAT
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data_json = self.get_json(response.data)

        self.assertEqual(response_data_json['name'], self.recipe_with_ingredients.name)
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

        response = self.client.patch(
            path=self.get_recipe_detail_url(recipe_id=self.recipe_with_ingredients.id),
            data=payload,
            format=API_CLIENT_JSON_FORMAT
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data_json = self.get_json(response.data)

        self.assertEqual(response_data_json['name'], self.recipe_with_ingredients.name)
        self.assertEqual(response_data_json['description'], self.recipe_with_ingredients.description)

        responser_data_ingredients = response_data_json['ingredients']
        self.assertEqual(len(responser_data_ingredients), 1)
        self.assertEqual(responser_data_ingredients[0]['name'], payload['ingredients'][0]['name'])

    def test_delete_recipe_with_ingredients(self):
        """Deleting recipe with ingredients in db successful"""
        response = self.client.delete(
            path=self.get_recipe_detail_url(recipe_id=self.recipe_with_ingredients.id)
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        ingredients_in_db = UtilsTestData.get_ingredients_from_db(recipe_id=self.recipe_with_ingredients.id)

        self.assertEqual(len(ingredients_in_db), 0)

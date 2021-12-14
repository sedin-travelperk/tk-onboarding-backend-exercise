from rest_framework import status

from recipes.tests.e2e.recipe_test_case import RecipeTestCase, API_CLIENT_JSON_FORMAT


class RecipeApiTests(RecipeTestCase):
    """Test recipe API"""

    def test_retrieve_recipe_list(self):
        """Retrieve recipe list from db successful"""

        response = self.client.get(
            path=self.get_recipe_url()
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)

    def test_create_recipe(self):
        """Creating recipe in db successful"""
        payload = {
            'name': 'Test recipe',
            'description': 'Test description',
        }

        response = self.client.post(
            path=self.get_recipe_url(),
            data=payload,
            format=API_CLIENT_JSON_FORMAT)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data_json = self.get_json(response.data)

        self.assertEqual(response_data_json['name'], payload['name'])
        self.assertEqual(response_data_json['description'], payload['description'])

    def test_update_recipe(self):
        """Updating recipe in db successful"""
        payload = {
            'name': 'New name'
        }

        response = self.client.patch(
            path=self.get_recipe_detail_url(recipe_id=self.recipe.id),
            data=payload,
            format=API_CLIENT_JSON_FORMAT)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data_json = self.get_json(response.data)

        self.assertEqual(response_data_json['name'], payload['name'])
        self.assertEqual(response_data_json['description'], self.recipe.description)

    def test_delete_recipe(self):
        """Deleting recipe from db"""
        response = self.client.delete(
            path=self.get_recipe_detail_url(recipe_id=self.recipe.id)
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

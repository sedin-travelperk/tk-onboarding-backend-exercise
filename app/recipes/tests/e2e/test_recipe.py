from rest_framework import status

from recipes.tests.e2e.recipe_test_case import RecipeTestCase, API_CLIENT_JSON_FORMAT

RECIPE_ID_NOT_PRESENT_IN_DB = 3124
NAME_NOT_IN_DB = 'hdsfjash'


class RecipeApiTests(RecipeTestCase):
    """Test recipe API"""

    def test_retrieve_recipe_list(self):
        """Retrieve recipe list from db successful"""

        response = self.client.get(
            path=self.get_recipe_url()
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)

    def test_retrieve_recipe_with_no_ingredients(self):
        """Retrieve recipe with no ingredients from db"""
        response = self.client.get(
            path=self.get_recipe_detail_url(recipe_id=self.recipe.id)
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.recipe.name)
        self.assertEqual(response.data['description'], self.recipe.description)
        self.assertEqual(len(response.data['ingredients']), 0)

    def test_retrieve_recipe_not_created(self):
        """Retrieve recipe that is not present in db"""
        response = self.client.get(
            path=self.get_recipe_detail_url(recipe_id=RECIPE_ID_NOT_PRESENT_IN_DB)
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

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
        self.assertEqual(response.data['name'], payload['name'])
        self.assertEqual(response.data['description'], payload['description'])

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
        self.assertEqual(response.data['name'], payload['name'])
        self.assertEqual(response.data['description'], self.recipe.description)

    def test_update_recipe_not_created(self):
        """Try to update recipe that is not present in db"""
        payload = {
            'name': "New name"
        }

        response = self.client.patch(
            path=self.get_recipe_detail_url(recipe_id=RECIPE_ID_NOT_PRESENT_IN_DB),
            data=payload,
            format=API_CLIENT_JSON_FORMAT
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_recipe(self):
        """Deleting recipe from db"""
        response = self.client.delete(
            path=self.get_recipe_detail_url(recipe_id=self.recipe.id)
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_recipe_not_created(self):
        """Try to delete recipe that is not present in db"""
        response = self.client.delete(
            path=self.get_recipe_detail_url(recipe_id=RECIPE_ID_NOT_PRESENT_IN_DB)
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_find_recipes_by_name_not_created(self):
        """Retrieve recipes from db by name that is not present in db"""
        querystring = {
            'name': NAME_NOT_IN_DB
        }

        response = self.client.get(
            path=self.get_recipe_url(),
            data=querystring
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_find_recipes_by_name(self):
        """Retrieve all recipes from db with given name"""
        querystring = {
            'name': self.recipe.name
        }

        response = self.client.get(
            path=self.get_recipe_url(),
            data=querystring
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.recipe.name)
        self.assertEqual(response.data[0]['description'], self.recipe.description)

    def test_find_recipes_by_name_substring(self):
        """Retrieve all recipes from db with given name substring"""
        querystring = {
            'name': self.recipe.name[:2]
        }

        response = self.client.get(
            path=self.get_recipe_url(),
            data=querystring
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

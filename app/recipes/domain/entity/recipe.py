"""All domain models for recipe feature should be in this file"""
import json


class Recipe:

    def __init__(self, name, description, recipe_id=None, ingredients=None):
        if ingredients is None:
            ingredients = []

        self.recipe_id = recipe_id
        self.name = name
        self.description = description
        self.ingredients = ingredients

    def update(self, **kwargs):
        name = kwargs.get('name', None)
        description = kwargs.get('description', None)

        if name:
            self.name = name

        if description:
            self.description = description

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def __str__(self):
        return f"{self.name} - {self.description}"

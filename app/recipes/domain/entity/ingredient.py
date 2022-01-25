class Ingredient:

    def __init__(self, name, ingredient_id=None):
        self.ingredient_id = ingredient_id
        self.name = name

    def to_json(self):
        return {
            "name": self.name
        }

    def __str__(self):
        return f"{self.name}"

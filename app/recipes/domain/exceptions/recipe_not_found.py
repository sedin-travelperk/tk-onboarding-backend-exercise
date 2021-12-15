class RecipeNotFound(Exception):
    def __init__(self, recipe_id):
        self.message = f'Recipe with id -> {recipe_id} not found!'
        super(RecipeNotFound, self).__init__(self.message)



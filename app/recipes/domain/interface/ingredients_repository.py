import abc
from typing import List

from recipes.domain.entity.ingredient import Ingredient


class IngredientRepository(abc.ABC):
    """Abstraction for Ingredient model"""

    @abc.abstractmethod
    def find_by_recipe_id(self, recipe_id: int) -> List[Ingredient]:
        raise NotImplemented

    @abc.abstractmethod
    def create(self, ingredient: Ingredient, recipe_id: int) -> Ingredient:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, ingredient_id: int) -> None:
        raise NotImplementedError

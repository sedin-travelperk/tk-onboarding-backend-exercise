import abc
from typing import List

from recipes.domain.entity.recipe import Recipe


class RecipeService(abc.ABC):
    """Abstraction for recipe service"""

    @abc.abstractmethod
    def get(self, recipe_id: int) -> Recipe:
        raise NotImplemented

    @abc.abstractmethod
    def find_all(self) -> List[Recipe]:
        raise NotImplemented

    @abc.abstractmethod
    def create(self, data: dict) -> Recipe:
        raise NotImplemented

    @abc.abstractmethod
    def update(self, recipe_id: int, data: dict) -> Recipe:
        raise NotImplemented

    @abc.abstractmethod
    def delete(self, recipe_id: int) -> None:
        raise NotImplemented

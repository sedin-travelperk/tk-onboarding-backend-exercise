import abc
from typing import List

from recipes.domain.entity.recipe import Recipe


class RecipeRepository(abc.ABC):
    """Abstraction for recipe persistence operations"""

    @abc.abstractmethod
    def get(self, recipe_id: int) -> Recipe:
        raise NotImplemented

    @abc.abstractmethod
    def find_all(self) -> List[Recipe]:
        raise NotImplemented

    @abc.abstractmethod
    def find_by_name(self, name: str) -> List[Recipe]:
        raise NotImplemented

    @abc.abstractmethod
    def create(self, recipe: Recipe) -> Recipe:
        raise NotImplemented

    @abc.abstractmethod
    def update(self, recipe: Recipe) -> Recipe:
        raise NotImplemented

    @abc.abstractmethod
    def delete(self, recipe_id: int) -> None:
        raise NotImplemented

    @abc.abstractmethod
    def exists(self, recipe_id: int) -> bool:
        raise NotImplemented

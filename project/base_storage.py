from exceptions import NotEnoughSpace, UnknownProduct, NotEnoughProduct
from project.abstract_storage import AbstractStorage


class BaseStorage(AbstractStorage):

    def __init__(self, items, capacity):
        self.__items = items
        self.__capacity = capacity

    def get_free_space(self) -> int:
        return self.__capacity - sum(self.__items.values())

    def add(self, name, amount):
        if self.get_free_space() < amount:
            raise NotEnoughSpace

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def remove(self, name: str, amount: int) -> None:
        if name not in self.__items:
            raise UnknownProduct
        if self.__items[name] < amount:
            raise NotEnoughProduct

        self.__items[name] -= amount
        if self.__items[name] == 0:
            del self.__items[name]

    @property
    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)

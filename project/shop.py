from exceptions import TooManyDifferentProducts
from project.base_storage import BaseStorage


class Shop(BaseStorage):
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name, amount):
        if name not in self.get_items and int(self.get_unique_items_count()) >= 5:
            raise TooManyDifferentProducts

        super().add(name, amount)

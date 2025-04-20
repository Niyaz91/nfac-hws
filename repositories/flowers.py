# repositories/flowers.py
from models import Flower

class FlowersRepository:
    def __init__(self):
        self.flowers = []
        self.counter = 1

    def add_flower(self, name, quantity, price):
        flower = Flower(self.counter, name, quantity, price)
        self.flowers.append(flower)
        self.counter += 1
        return flower

    def list_flowers(self):
        return self.flowers

    def find_by_id(self, id):
        return next((f for f in self.flowers if f.id == id), None)

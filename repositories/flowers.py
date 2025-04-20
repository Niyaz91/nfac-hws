from models import Flower

class FlowersRepository:
    def __init__(self):
        self.flowers = []
        self.counter = 1

    def add_flower(self, name: str, price: float):
        flower = Flower(id=self.counter, name=name, price=price)
        self.flowers.append(flower)
        self.counter += 1
        return flower.id

    def list_flowers(self):
        return self.flowers

    def get_by_id(self, flower_id: int):
        return next((f for f in self.flowers if f.id == flower_id), None)

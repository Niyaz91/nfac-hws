from pydantic import BaseModel
from typing import List, Optional

class User:
    def __init__(self, id, email, name, password, photo=None):
        self.id = id
        self.email = email
        self.name = name
        self.password = password

class Flower:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

class Purchase:
    def __init__(self, user_id, flower_id):
        self.user_id = user_id
        self.flower_id = flower_id

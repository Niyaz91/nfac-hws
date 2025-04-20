class User:
    def __init__(self, username, password_hash, photo: bytes = None):
        self.username = username
        self.password_hash = password_hash

class Flower:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

class Purchase:
    def __init__(self, user_id: str, flower_id: int):
        self.user_id = user_id
        self.flower_id = flower_id

# repositories/users.py
from models import User

class UsersRepository:
    def __init__(self):
        self.users = []
        self.counter = 1

    def add_user(self, email, name, password, photo=None):
        user = User(self.counter, email, name, password, photo)
        self.users.append(user)
        self.counter += 1
        return user

    def find_by_email(self, email):
        return next((u for u in self.users if u.email == email), None)

    def find_by_id(self, user_id):
        return next((u for u in self.users if u.id == user_id), None)

from models import User

class UsersRepository:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password_hash):
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = User(username, password_hash)

    def get_user(self, username):
        return self.users.get(username)

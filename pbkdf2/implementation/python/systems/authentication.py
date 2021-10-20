from adapters.json import JsonAdapter
from models.user import User
from config import config
import os

class AuthenticationSystem (System):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not kwargs.get("db"):
            self.db = JsonAdapter.connect("db.json", fields = { "username": str, "password": str , "salt": str }, consistent = True))

    def authenticateUser (self, username, password):
        users = filter((lambda u: u.hasPassword(password, algorithm = self.algorithm, peppers = self.peppers))), self.db.fetch({"username": username}))
        return users.next()

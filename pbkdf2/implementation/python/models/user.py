from models.model import Model
from copy import copy


class UserModel(Model):
    __fields = {}

    def __init__(self, username, password="", salt=""):
        self.__fields = {"username": username, "password": password, "salt": salt}

    def __getitem__(self, key):
        return copy(self.__fields[key])

    def __setitem__(self, key, value):
        if key in self.__fields.keys():
            self.__fields[key] = value

    @property
    def fields(self):
        return self.__fields.items()

    def hasPassword(self, plaintext, algorithm, peppers=[]):
        return any(
            algorithm.encrypt(
                algorithm.deriveKey(plaintext),
                salt=self.__fields["salt"],
                pepper=pepper,
            )
            == self.__fields["password"]
            for pepper in peppers
        )

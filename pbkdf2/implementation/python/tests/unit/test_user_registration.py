from config import Config
from adapters.json import JsonAdapter
from systems.registration import RegistrationSystem
import unittest


class Config(Config):
    database = "test.json"


config = Config()


class TestRegistrationSystem(unittest.TestCase):
    user_details = {"username": "test_user", "password": "locked"}

    def test_user_registration(self):
        database = JsonAdapter.connect(config.database)
        database.open()
        database.read()
        # system = RegistrationSystem()

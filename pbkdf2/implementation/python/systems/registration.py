from adapters.json import JsonAdapter
from models.user import UserModel
from serializers.json import JsonSerializer
from systems.system import System
from config import config


class ExistentUserError(Exception):
    def __init__(self):
        print("A user having the username already exists")


class RegistrationSystem(System):
    __is_initiated = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not kwargs.get("db"):
            self.db = JsonAdapter.connect(
                config.database,
                fields={"username": str, "password": str, "salt": str},
                consistent=True,
            )
        if not kwargs.get("serializer"):
            self.serializer = JsonSerializer

    def initiate(self):
        self.algorithm = self.algorithm()
        self.serializer = self.serializer()
        self.db.open()
        self.db.read()
        self.__is_initiated = True

    def registerUser(self, username, password):
        assert (
            self.__is_initiated
        ), "You must initiate the system before registering users"

        if any(filter(lambda u: u["username"] == username, self.users)):
            raise ExistentUserError()

        salt = self.algorithm.getSalt()
        key = self.algorithm.deriveKey(password)
        user = UserModel(
            username,
            password=self.algorithm.encrypt(key, salt=salt, peppers=self.peppers),
            salt=salt,
        )
        userData = self.serializer.serialize(user)
        userData["password"] = userData["password"].hex()
        userData["salt"] = userData["salt"].hex()
        self.db.write(userData)
        self.db.save()
        return user

    def getUser(self, username):
        users = list(filter(lambda u: u["username"] == username, self.users))
        if users:
            return users[0]

    def loginUser(self, username, password):
        userRecord = self.getUser(username)
        if not (userRecord):
            return False

        user = UserModel(**userRecord)
        user["password"] = bytes.fromhex(user["password"])
        user["salt"] = bytes.fromhex(user["salt"])
        if user.hasPassword(password, self.algorithm, peppers=self.peppers):
            return user

    @property
    def users(self):
        return self.db.fetch()

    def shutdown(self):
        self.__is_initiated = False

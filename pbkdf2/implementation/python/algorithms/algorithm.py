from abc import ABC, abstractmethod


class Algorithm(ABC):
    @abstractmethod
    def deriveKey(self, plaintext):
        pass

    @abstractmethod
    def encrypt(self, key, salt="", peppers=[]):
        pass

    @abstractmethod
    def getSalt(self):
        pass

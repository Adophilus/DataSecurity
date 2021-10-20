from algorithms.algorithm import Algorithm
from config import config

import os
import random
import hashlib


class DefaultAlgorithm(Algorithm):
    def __init__(self, salt_length=32, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.salt_length = salt_length
        self.encoding = config.encoding

    def deriveKey(self, plaintext):
        return hashlib.sha256(plaintext.encode(self.encoding)).digest()

    def encrypt(self, key, salt="", peppers=config.peppers, pepper=None):
        if pepper:
            return hashlib.sha512(salt + key + pepper).digest()
        return hashlib.sha512(salt + key + random.choice(peppers)).digest()

    def getSalt(self):
        return os.urandom(self.salt_length)

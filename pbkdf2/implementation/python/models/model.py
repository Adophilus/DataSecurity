from abc import ABC, abstractmethod


class Model(ABC):
    @property
    def fields(self):
        return [[]]

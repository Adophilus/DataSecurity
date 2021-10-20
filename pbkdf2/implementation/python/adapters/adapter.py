from abc import ABC, abstractmethod


class Adapter(ABC):
    class Connection(ABC):
        def __init__(self, write_on_save=False):
            self.write_on_save = write_on_save

        @abstractmethod
        def close(self):
            pass

        @abstractmethod
        def empty(self):
            pass

        @abstractmethod
        def fetch(self, **kwargs):
            pass

        @abstractmethod
        def open(self):
            pass

        @abstractmethod
        def read(self):
            pass

        @abstractmethod
        def save(self):
            pass

        @abstractmethod
        def write(self, data):
            pass

    @classmethod
    @abstractmethod
    def connect(cls, file):
        pass

from abc import ABC, abstractmethod
from adapters.json import JsonAdapter
from algorithms.default import DefaultAlgorithm
from config import config


class System(ABC):
    def __init__(
        self,
        peppers=config.peppers,
        algorithm=DefaultAlgorithm,
        db=JsonAdapter.connect("db.json"),
    ):
        self.algorithm = algorithm
        self.peppers = peppers
        self.db = db

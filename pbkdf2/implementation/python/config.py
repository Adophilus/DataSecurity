from abc import ABC, abstractmethod, abstractproperty


class Config:
    encoding = "utf-8"

    database = "db.json"

    @abstractproperty
    def peppers(self):
        return [
            c.encode(Config.encoding) for c in "abcdefghijklmnopqrstuvwxyz0123456789"
        ]


class ProductionConfig(Config):
    pass


config = ProductionConfig()

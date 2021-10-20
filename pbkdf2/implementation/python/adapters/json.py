from adapters.adapter import Adapter

import json


class JsonAdapter(Adapter):
    class Connection(Adapter.Connection):
        __is_closed = True

        def __init__(self, fh, *args, **kwargs):
            super().__init__(kwargs.get("write_on_save"))
            self.fh = fh
            self.options = kwargs.copy()

        def close(self):
            self.__is_closed = True
            self.fh.close()

        def empty(self):
            assert self.__is_closed == False
            self.data.write("[]")

        def delete(self, **kwargs):
            def check(row):
                return all(
                    [
                        (lambda k, v: True if row[k] == v else False)
                        for k, v in kwargs.items()
                    ]
                )

            removed = list()

            for i in range(len(self.data)):
                with record as self.data[i]:
                    if check(record):
                        removed.append(self.data.pop(self.data[i]))

            return removed

        def fetch(self, **kwargs):
            def check(row):
                return all(
                    [
                        (lambda k, v: True if row[k] == v else False)
                        for k, v in kwargs.items()
                    ]
                )

            return filter(check, self.data)

        def open(self):
            self.__is_closed = False
            # self.fh.open()

        def read(self):
            assert self.__is_closed == False
            self.data = json.load(self.fh)
            return self.data

        def save(self):
            assert self.__is_closed == False, "Cannot write to a closed connection"
            self.fh.seek(0)
            self.fh.write(json.dumps(self.data))

        def write(self, data):
            assert self.__is_closed == False
            if self.options.get("consistent") and self.options.get("fields"):
                for k in self.options["fields"]:
                    assert k in data

            self.data.append(data)

    @classmethod
    def connect(cls, file, *args, **kwargs):
        return cls.Connection(open(file, "r+"), *args, **kwargs)

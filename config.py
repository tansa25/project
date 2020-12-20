from abc import ABC, abstractmethod
import json


class IConfig(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def update(self, key, value):
        pass


class LocalConfig(IConfig):
    def __init__(self, path):
        self.path = path
        self.data = None
        self.load()

        if self.get('companies') is None:
            self.update('companies', {})

    def load(self):
        with open(self.path, 'r+') as file:
            text = file.read()
            if text:
                self.data = json.loads(text)
            else:
                self.data = {}

    def save(self):
        with open(self.path, 'w') as file:
            file.write(json.dumps(self.data))

    def get(self, key):
        if not(key in self.data):
            self.update(key, None)

        return self.data[key]

    def update(self, key, value):
        self.data[key] = value
        self.save()

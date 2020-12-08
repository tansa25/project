from abc import ABC, abstractmethod


class IConfig(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def update(self, key, value):
        pass

    @abstractmethod
    def reset(self):
        pass

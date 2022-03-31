from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def make_title(self, title):
        pass

    @abstractmethod
    def make_string(self, s):
        pass

    @abstractmethod
    def make_items(self, items):
        pass

    @abstractmethod
    def close():
        pass

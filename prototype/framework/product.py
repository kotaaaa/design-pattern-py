from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def use(self, s):
        pass

    @abstractmethod
    def create_clone(self):
        pass

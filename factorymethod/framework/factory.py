from abc import ABCMeta, abstractmethod


class Factory(metaclass=ABCMeta):
    def create(self, owner):
        p = self.create_product(owner)
        self.register_product(p)
        return p

    @abstractmethod
    def create_product(self, owner):
        pass

    @abstractmethod
    def register_product(self, product):
        pass

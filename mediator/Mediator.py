from abc import ABCMeta, abstractmethod


class Mediator(metaclass=ABCMeta):
    def create_colleagues(self):
        pass

    def colleagues_changed(self):
        pass

from abc import ABCMeta, abstractmethod


class Collegue(metaclass=ABCMeta):
    def set_mediator(self, mediator):
        pass

    def set_colleague_enabled(self, enabled):
        pass

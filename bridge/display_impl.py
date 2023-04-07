from abc import ABCMeta, abstractmethod


class DisplayImpl(metaclass=ABCMeta):
    def raw_open(self):
        pass

    def raw_print(self):
        pass

    def raw_close(self):
        pass

from abc import ABCMeta, abstractmethod


class Entry(metaclass=ABCMeta):
    @abstractmethod
    def get_name():
        pass

    @abstractmethod
    def get_size():
        pass

    def add(self, entry):
        raise Exception

    def print_list(self):
        _print_list("")

    @abstractmethod()
    def _print_list(prefix):  # protected method
        pass

    def to_string(self):
        return get_name() + " (" + get_size() + ")"

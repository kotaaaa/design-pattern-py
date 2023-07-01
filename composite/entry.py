from abc import ABCMeta, abstractmethod
from file_treatment_exception import FileTreatmentException


class Entry(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    def add(self, entry):
        raise FileTreatmentException("Error: Don't use add method to File object!")

    def print_list(self):
        self._print_list("")

    @abstractmethod
    def _print_list(self, prefix):  # protected method
        pass

    def to_string(self):
        return self.get_name() + " (" + str(self.get_size()) + ")"

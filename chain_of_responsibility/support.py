from abc import ABCMeta, abstractmethod


class Support(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    def set_next(self, next):
        self.next = next
        return self.next

    def support(trouble):
        if self.resolve(trouble):
            done(trouble)
        elif self.next is not None:
            self.next.support(trouble)
        else:
            self.fail(trouble)

    def to_string(self):
        return "[" + self.name + "]"

    @abstractmethod
    def resolve(self):
        pass

    def done(self, trouble):
        print(self.trouble + " is resolved by " + this + ".")

    def fail(self, trouble):
        print(self.trouble + "cannot be resolved.")

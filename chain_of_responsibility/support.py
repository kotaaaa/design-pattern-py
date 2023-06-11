from abc import ABCMeta, abstractmethod


class Support(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        self.next = next
        return self.next

    def support(self, trouble):
        if self.resolve(trouble):
            self.done(trouble)
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
        print(trouble.to_string() + " is resolved by " + self.name + ".")

    def fail(self, trouble):
        print(trouble.to_string(), " cannot be resolved.")

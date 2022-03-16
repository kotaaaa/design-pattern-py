import copy

from framework.manager import Manager
from framework.product import Product


class MessageBox(Product):
    def __init__(self, decochar):
        self.decochar = decochar

    def use(self, s):
        length = len(s)
        for i in range(length + 4):
            print(self.decochar, end="")
        print()
        print(self.decochar + " " + s + " " + self.decochar)
        for i in range(length + 4):
            print(self.decochar, end="")
        print()

    def create_clone(self):
        p = MessageBox(self.decochar)
        return copy.deepcopy(p)

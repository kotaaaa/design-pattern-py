import copy

from framework.manager import Manager
from framework.product import Product


class UnderlinePen(Product):
    def __init__(self, ulchar):
        self.ulchar = ulchar

    def use(self, s):
        length = len(s)
        print('"' + s + '"')
        print(" ", end="")

        for i in range(length):
            print(self.ulchar, end="")

        print()

    def create_clone(self):
        p = UnderlinePen(self.ulchar)
        return copy.deepcopy(p)

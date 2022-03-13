from framework.factory import Factory
from framework.product import Product


class IDCard(Product):
    def __init__(self, owner, serial):
        self.owner = owner
        self.serial = serial
        print(self.owner + "(" + str(self.serial) + ")" + "'s card is created.")

    def use(self):
        print(self.owner + "(" + str(self.serial) + ")" + "'s card is used.")

    def get_owner(self):
        return self.owner

    def get_serial(self):
        return self.serial

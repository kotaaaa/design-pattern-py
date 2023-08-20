# from threading import RLock
from framework.factory import Factory
from framework.product import Product
from idcard.idcard import IDCard


class IDCardFactory(Factory):
    def __init__(self):
        self.database = {}
        self.serial = 100

    def create_product(self, owner):
        # with self.lock:
        return IDCard(owner, self.serial + 1)

    def register_product(self, product):
        # with self.lock:
        self.database.update({product.get_serial(): product.get_owner()})

    def get_database(self):
        return self.database

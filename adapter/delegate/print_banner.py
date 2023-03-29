from banner import Banner
from print import Print


class PrintBanner(Print):
    def __init__(self, string):
        self.banner = Banner(string)

    def print_weak(self):
        self.banner.show_with_paren()

    def print_strong(self):
        self.banner.show_with_aster()

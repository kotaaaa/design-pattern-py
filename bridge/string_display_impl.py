from display_impl import DisplayImpl


class StringDisplayImpl(DisplayImpl):
    def __init__(self, string):
        self.string = string
        self.width = len((string).encode("utf-8"))

    def raw_open(self):
        self.print_line()

    def raw_print(self):
        print("|" + self.string + "|")

    def raw_close(self):
        self.print_line()

    def print_line(self):
        print("+", end="")
        for i in range(self.width):
            print("-", end="")
        print("+")

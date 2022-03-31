from builder import Builder


class TextBuilder(Builder):
    def __init__(self):
        self.buffer = ""

    def make_title(self, title):
        self.buffer += "==============================\n"
        self.buffer += "『" + title + "』"
        self.buffer += "\n"

    def make_string(self, s):
        self.buffer += "■" + s + "\n"
        self.buffer += "\n"

    def make_items(self, items):
        for item in items:
            self.buffer += " ・" + item + "\n"
        self.buffer += "\n"

    def close(self):
        self.buffer += "==============================\n"

    def get_result(self):
        return self.buffer

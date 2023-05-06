class StringDisplay(Display):
    def __init__(self, string):
        self.string = string

    def get_columns(self):
        return len(self.string.encode("utf-8"))

    def get_rows(self):
        return 1

    def get_row_text(self, row):
        if row == 0:
            return self.string
        else:
            None

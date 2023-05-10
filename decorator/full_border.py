from border import Border

class FullBorder(Border):
    def __init__(self, display):
        super().__init__(display)

    def get_columns(self):
        return 1 + self.display.get_columns() + 1

    def get_rows(self):
        return 1 + self.display.get_rows() + 1

    def get_row_text(self, row):
        if row == 0:
            return "+" + self.make_line("-", self.display.get_columns()) + "+"
        elif row == self.display.get_rows() + 1:
            return "+" + self.make_line("-", self.display.get_columns()) + "+"
        else:
            return "|" + self.display.get_row_text(row - 1) + "|"

    def make_line(self, ch, count):
        buf = ""
        for i in range(count):
            buf += ch
        return buf

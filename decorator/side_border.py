class SideBorder(Border):
    def __init__(self, display, ch):
        super().__init__(display)
        self.border_char = ch

    def get_columns(self):
        return 1 + self.display.get_columns() + 1

    def get_rows(self):
        self.display.get_rows()

    def get_row_text(self, row):
        return self.border_char + self.display.get_row_text(row) + border_char

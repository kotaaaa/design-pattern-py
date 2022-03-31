from factory.tray import Tray


class ListTray(Tray):
    def __init__(self, caption):
        super().__init__(caption)

    def make_html(self):
        buffer = ""
        buffer += "<li>\n"
        buffer += self.caption + "\n"
        buffer += "<ul>\n"

        for t in self.tray:
            buffer += t.make_html()
        buffer += "</ul>\n"
        buffer += "</li>\n"

        return buffer

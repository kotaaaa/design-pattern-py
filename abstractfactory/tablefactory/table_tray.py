from factory.tray import Tray


class TableTray(Tray):
    def __init__(self, caption):
        super().__init__(caption)

    def make_html(self):
        buffer = ""
        buffer += "<td>"
        buffer += '<table width="100%" border="1"><tr>'
        buffer += (
            '<td bgcolor="#cccccc" align="center" colspan="'
            + str(len(self.tray))
            + '"><b>'
            + self.caption
            + "</b></td>"
        )
        buffer += "</tr>\n"
        buffer += "<tr>\n"

        for t in self.tray:
            buffer += t.make_html()

        buffer += "</tr></table>"
        buffer += "</td>"
        return buffer

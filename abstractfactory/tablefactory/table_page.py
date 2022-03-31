from factory.page import Page


class TablePage(Page):
    def __init__(self, title, auther):
        super().__init__(title, auther)

    def make_html(self):
        buffer = ""
        buffer += "<html><head><title>" + self.title + "</title></head>\n"
        buffer += "<body>\n"
        buffer += "<h1>" + self.title + "</h1>\n"
        buffer += '<table width="80%" border="3">\n'
        for t in self.content:
            buffer += "<tr>" + t.make_html() + "</tr>"
        buffer += "</table>\n"
        buffer += "<hr><address>" + self.auther + "</address>"
        buffer += "</body></html>\n"
        return buffer

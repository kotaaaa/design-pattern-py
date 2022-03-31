from factory.page import Page


class ListPage(Page):
    def __init__(self, title, auther):
        super().__init__(title, auther)

    def make_html(self):
        buffer = ""
        buffer += "<html><head><title>" + self.title + "</title></head>\n"
        buffer += "<body>\n"
        buffer += "<h1>" + self.title + "</h1>\n"
        buffer += "<ul>\n"

        for c in self.content:
            buffer += c.make_html()

        buffer += "</ul>\n"
        buffer += "<hr><address>" + self.auther + "</address>"
        buffer += "</body></html>\n"

        return buffer

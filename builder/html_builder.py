from builder import Builder


class HtmlBuilder(Builder):
    # def __init__(self):
    # f = open(")
    def __init__(self):
        self.f = ""
        self.filename = ""

    def make_title(self, title):

        self.filename = title + ".html"
        self.f = open(self.filename, "w")
        self.f.write("<html><head><title>" + title + "</title></head><body>\n")
        self.f.write("<h1>" + title + "</h1>\n")

    def make_string(self, s):
        self.f.write("<p>" + s + "</p>\n")

    def make_items(self, items):
        self.f.write("<ul>\n")
        for item in items:
            self.f.write("<li>" + item + "</li>\n")
        self.f.write("</ul>\n")

    def close(self):
        self.f.write("</body></html>\n")
        self.f.close()

    def get_result(self):
        return self.filename

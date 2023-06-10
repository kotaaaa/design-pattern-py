class HtmlWriter:
    def __init__(self, writer):
        self.writer = writer

    def title(self, title):
        self.writer.write("<html>")
        self.writer.write("<head>")
        self.writer.write("<title>" + title + "</title>")
        self.writer.write("</head>")
        self.writer.write("<body>\n")
        self.writer.write("<h1>" + title + "<h1>")
        self.writer.write("<html>")

    def paragraph(self, msg):
        self.writer("<p>" + msg + "</p>\n")

    def link(href, caption):
        paragraph('<a href="' + href + '">' + caption + "</a>")

    def mailto(self, mailaddr, username):
        link("mailto: " + mailaddr, username)

    def close(self):
        writer.write("</body>")
        writer.write("</html>\n")
        writer.close()

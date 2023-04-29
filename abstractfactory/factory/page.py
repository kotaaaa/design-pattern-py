from abc import ABCMeta, abstractmethod


class Page:
    def __init__(self, title, auther):
        self.title = title
        self.auther = auther
        self.content = []

    def add(self, item):
        self.content.append(item)

    def output(self):
        filename = self.title + ".html"
        with open(filename, "w") as f:
            f.write(self.make_html())
            print(filename + "を作成しました")

    @abstractmethod
    def make_html(self):
        pass

from listfactory.list_link import ListLink
from listfactory.list_tray import ListTray
from listfactory.list_page import ListPage
from factory.factory import Factory


class ListFactory(Factory):
    def create_link(self, caption, url):
        return ListLink(caption, url)

    def create_tray(self, caption):
        return ListTray(caption)

    def create_page(self, title, auther):
        return ListPage(title, auther)

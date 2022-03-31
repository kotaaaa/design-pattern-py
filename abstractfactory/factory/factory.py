from abc import ABCMeta, abstractmethod


class Factory(metaclass=ABCMeta):
    def __init__(self, factory):
        self.factory = factory

    def get_factory(self, classname):
        return ""  # TODO class forname でクラス名を動的に取得する。

    @abstractmethod
    def create_link(self, caption, url):
        pass

    @abstractmethod
    def create_tray(self, caption):
        pass

    @abstractmethod
    def create_page(self, title, auther):
        pass

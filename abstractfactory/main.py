from factory.factory import Factory
from listfactory.list_factory import ListFactory
from tablefactory.table_factory import TableFactory
import sys


def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python main.py class.name.of.ConcreteFactory")
        print("Example 1: python main.py list_factory.ListFactory")
        print("Example 2: python main.py table_factory.TableFactory")

    # TODO クラス名を動的に渡して該当クラスのFactory インスタンスを作成する。
    factory = ListFactory("list_factory.ListFactory")
    # factory = TableFactory("list_factory.ListFactory")
    asahi = factory.create_link("朝日新聞", "http//www.asahi.com/")
    yomiuri = factory.create_link("読売新聞", "http//www.yomiuri.co.jp/")
    us_yahoo = factory.create_link("Yahoo!", "http//www.yahoo.com/")
    jp_yahoo = factory.create_link("Yahoo!Japan", "http//www.yahoo.co.jp/")
    excite = factory.create_link("Excite", "http//www.excite.com/")
    google = factory.create_link("Google", "http//www.google.com/")

    traynews = factory.create_tray("新聞")
    traynews.add(asahi)
    traynews.add(yomiuri)

    trayyahoo = factory.create_tray("Yahoo!")
    trayyahoo.add(us_yahoo)
    trayyahoo.add(jp_yahoo)

    traysearch = factory.create_tray("サーチエンジン")
    traysearch.add(trayyahoo)
    traysearch.add(excite)
    traysearch.add(google)

    page = factory.create_page("TablePage", "個人名")
    page.add(traynews)
    page.add(traysearch)

    page.output()


if __name__ == "__main__":
    main()

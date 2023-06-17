import sys
from html_builder import HtmlBuilder
from text_builder import TextBuilder
from director import Director


def main():
    args = sys.argv
    if len(args) != 2:
        usage()
        exit(0)

    if args[1] == "plain":
        text_builder = TextBuilder()
        director = Director(text_builder)
        director.construct()
        result = text_builder.get_result()
        print(result)

    elif args[1] == "html":
        html_builder = HtmlBuilder()
        director = Director(html_builder)
        director.construct()
        filename = html_builder.get_result()
        print(filename + "が作成されました.")
    else:
        usage()
        exit(0)


def usage():
    print("Usage: python main.py plain  プレーンテキストで文書作成")
    print("Usage: python main.py html  HTMLファイルで文書作成")


if __name__ == "__main__":
    main()

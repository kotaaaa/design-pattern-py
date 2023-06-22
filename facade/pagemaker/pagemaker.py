from database import Database
from pagemaker.html_writer import HtmlWriter


class PageMaker:
    def __init__(self):
        pass

    @classmethod
    def make_welcome_page(self, mailaddr, filename):
        try:
            mailprop = Database.get_proprties("maildata")
            username = mailprop["section1"][mailaddr]
            f = open(filename, "w")
            writer = HtmlWriter(f)
            writer.title("Welcome to " + username + "'s page!")
            writer.paragraph("I am waiting a email.")
            writer.mailto(mailaddr, username)
            writer.close()
            print(filename + " is created for " + mailaddr + " (" + username + ")")
        except Exception as e:
            print("Exception Occured. ", e)

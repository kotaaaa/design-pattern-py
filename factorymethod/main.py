from idcard.idcardfactory import IDCardFactory


def main():
    factory = IDCardFactory()
    card1 = factory.create("James")
    card2 = factory.create("Mike")
    card3 = factory.create("Harvey")
    card1.use()
    card2.use()
    card3.use()

if __name__ == "__main__":
    main()

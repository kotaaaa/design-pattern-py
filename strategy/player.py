from strategy import Strategy


class Player:
    wincount = 0
    losecount = 0
    gamecount = 0

    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy

    def next_hand(self):
        return self.strategy.next_hand()

    def win(self):
        self.strategy.study(True)
        self.wincount += 1
        self.gamecount += 1

    def lose(self):
        self.strategy.study(False)
        self.losecount += 1
        self.gamecount += 1

    def even(self):
        self.gamecount += 1

    def to_string(self):
        return (
            "["
            + self.name
            + ": "
            + str(self.gamecount)
            + " games, "
            + str(self.wincount)
            + " win, "
            + str(self.losecount)
            + " lose"
            + "]"
        )

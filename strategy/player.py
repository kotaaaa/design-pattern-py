from strategy import Strategy


class Player:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy

    def next_hand(self):
        return self.stratery.next_hand()

    def win(self):
        self.strategy(true)
        wincount += 1
        gamecount += 1

    def lose(self):
        self.strategy(false)
        losecount += 1
        gamecount += 1

    def even(self):
        gamecount += 1

    def to_string(self):
        return (
            "["
            + name
            + ":"
            + gamecount
            + " games, "
            + wincount
            + " win, "
            + losecount
            + " lose"
            + "]"
        )

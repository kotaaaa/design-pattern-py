from strategy import Strategy
import random
from hand import Hand


class WinningStrategy(Strategy):
    pre_hand = Hand(1)
    won = False

    def __init__(self, seed):
        self.random = random.randint(0, 2)

    def next_hand(self):
        if not self.won:
            self.pre_hand = Hand.get_hand(random.randint(0, 2))
        return self.pre_hand

    def study(self, win):
        self.won = win

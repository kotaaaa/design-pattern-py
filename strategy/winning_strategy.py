from strategy import Strategy
import random


class WinningStrategy(Strategy):
    won = false

    def __init__(self, seed):
        self.random = random.randint(0, 2)

    def next_hand(self):
        if not won:
            pre_hand = Hand.get_hand(self.random.nextInt(3))
        return pre_hand

    def study(self, win):
        won = win

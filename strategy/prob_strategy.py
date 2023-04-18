from strategy import Strategy
import random


class ProbStrategy(Strategy):
    history = [[1 for i in range(3)] for j in range(3)]

    def __init__(self, seed):
        self.random = random.randint(0, 2)

    def next_hand(self):
        bet = random.randint(0, get_sum(current_hand_value))
        hand_value = 0

        return Hand.get_hand(hand_value)

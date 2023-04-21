from strategy import Strategy
import random
from hand import Hand


class ProbStrategy(Strategy):
    history = [[1 for i in range(3)] for j in range(3)]
    current_hand_value = 0
    prev_hand_value = 0

    def __init__(self, seed):
        self.random = random.randint(0, 2)

    def next_hand(self):
        bet = random.randint(0, self.get_sum(self.current_hand_value))
        hand_value = 0
        if bet < self.history[self.current_hand_value][0]:
            hand_value = 0
        elif (
            bet
            < self.history[self.current_hand_value][0]
            + self.history[self.current_hand_value][1]
        ):
            hand_value = 1
        else:
            hand_value = 2
        self.prev_hand_value = self.current_hand_value
        self.current_hand_value = hand_value
        return Hand.get_hand(hand_value)

    def get_sum(self, hv):
        sum = 0
        for i in range(3):
            sum += self.history[hv][i]
        return sum

    def study(self, win):
        if win:
            self.history[self.prev_hand_value][self.current_hand_value] += 1
        else:
            self.history[self.prev_hand_value][(self.current_hand_value + 1) % 3] += 1
            self.history[self.prev_hand_value][(self.current_hand_value + 2) % 3] += 1

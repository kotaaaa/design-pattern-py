class Hand:
    HANDVALUE_GUU = 0
    HANDVALUE_CHO = 1
    HANDVALUE_PAA = 2

    hand = [Hand(0), Hand(1), Hand(2)]

    name = ["Rock", "Scissors", "Paper"]

    def __init__(self, handvalue):
        self.handvalue = handvalue

    def get_hand(self, handvalue):
        return hand[handvalue]

    def is_stronger_than(self, h):
        return fight(h) == 1

    def is_weaker_than(self, h):
        return fight(h) == -1

    def fight(self, h):
        if self == h:
            return 0
        elif (this.handvalue + 1) % 3 == h.handvalue:
            return 1
        else:
            return -1

    def to_string(self):
        return name[self.handvalue]

def add_instance(cls):
    cls.hand.append(cls(cls.HANDVALUE_GUU))
    cls.hand.append(cls(cls.HANDVALUE_CHO))
    cls.hand.append(cls(cls.HANDVALUE_PAA))
    return cls


@add_instance
class Hand:
    HANDVALUE_GUU = 0
    HANDVALUE_CHO = 1
    HANDVALUE_PAA = 2
    name = ["Rock", "Scissors", "Paper"]
    hand = []

    def __init__(self, handvalue):
        self.handvalue = handvalue

    @classmethod
    def get_hand(cls, handvalue):
        return cls.hand[handvalue]

    def is_stronger_than(self, h):
        return self.fight(h) == 1

    def is_weaker_than(self, h):
        return self.fight(h) == -1

    def fight(self, h):
        if self == h:
            return 0
        elif (self.handvalue + 1) % 3 == h.handvalue:
            return 1
        else:
            return -1

    def to_string(self):
        return name[self.handvalue]

from no_support import NoSupport
from limit_support import LimitSupport
from special_support import SpecialSupport
from odd_support import OddSupport
from limit_support import LimitSupport
from trouble import Trouble


def main():
    # args = sys.argv
    # if len(args) != 2:
    alice = NoSupport("Alice")
    bob = LimitSupport("Bob", 100)
    charlie = SpecialSupport("Tom", 429)
    elmo = OddSupport("Elmo")
    fred = LimitSupport("Fred", 300)

    alice.set_next(bob).set_next(charlie).set_next(elmo).set_next(fred)

    for i in range(0, 500, 33):
        alice.support(Trouble(i))


if __name__ == "__main__":
    main()

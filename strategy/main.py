from player import Player
from winning_strategy import WinningStrategy
from prob_strategy import ProbStrategy
import sys


def main():
    args = sys.argv
    if len(args) != 3:
        print("Usage: python main.py randomseed1 randomseed2")
        print("Example: python main.py 314 15")
        exit()

    seed1 = int(args[1])
    seed2 = int(args[2])
    player1 = Player("Taro", WinningStrategy(seed1))
    player2 = Player("Hana", ProbStrategy(seed2))
    for i in range(10000):
        nexthand1 = player1.next_hand()
        nexthand2 = player2.next_hand()
        if nexthand1.is_stronger_than(nexthand2):
            print("Winner: ", player1.to_string())
            player1.win()
            player2.lose()
        elif nexthand2.is_stronger_than(nexthand1):
            print("Winner:", player2.to_string())
            player1.lose()
            player2.win()
        else:
            print("Even..")
            player1.even()
            player2.even()
    print("Total result: ")
    print(player1.to_string())
    print(player2.to_string())


if __name__ == "__main__":
    main()

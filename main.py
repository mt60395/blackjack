# Blackjack
import random

balance = 1000  # the current balance one has
bet = 0  # the current bet one has placed
cards = []  # card deck is refreshed every round and stored so we don't have duplicates.
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]  # categories

player = []  # to store the current hand's cards
cpu = []


def make_bet():  # betting function.
    bet = balance + 1
    while bet > balance:
        print("Your current balance is: " + str(balance))
        bet = int(input("Enter a bet (must be less than or equal to your current balance): "))


def refresh_deck():
    # Add the numbered ranks before the special ranks
    cards = []
    for i in suits:  # four different sets
        for j in ranks:
            cards.append(j + " of " + i)
    # print(cards)
    # print(len(cards))
    player = []
    cpu = []


def new_round(rounds):
    print("Round " + str(rounds))
    make_bet()
    refresh_deck()
    new_card()


def new_card():
    index = random.randint(0, 51)  # random card.
    # TODO: make iterable or something
    player.append(cards.pop(index))


def main():
    rounds = 0  # rounds elapsed
    while True:
        new_round(rounds)
        rounds += 1


if __name__ == "__main__":
    main()

# Blackjack

balance = 50  # the current balance one has
bet = 0  # the current bet one has placed

def make_bet():  # betting function.
    bet = balance + 1
    while (bet > balance):
        print("Your current balance is: " + balance)
        bet = int(input("Enter a bet (must be less than or equal to your current balance): "))

def main():
    make_bet()

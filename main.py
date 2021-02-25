# Blackjack
import random

balance = 1000  # the current balance one has
bet = 0  # the current bet one has placed
cards = []  # card deck is refreshed every round and stored so we don't have duplicates.
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
rank_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # corresponding rank values with all the ranks
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]  # categories to create cards with

player = []  # to store the current hand's cards
dealer = []  # to store the cpu's cards. it's a 1v1
dealer_hidden = []  # dealer's face down card, which is pulled before the first round.
player_score = 0  # current scores
dealer_score = 0


def make_bet():  # betting function.
    global balance, bet
    bet = balance + 1
    while bet > balance:
        print("Your current balance is: " + str(balance))
        bet = int(input("Enter a bet (must be less than or equal to your current balance): "))
    balance -= bet
    # Bets are automatically taken away. If one loses, nothing happens. If you win, you get back your bet,
    # multiplied by a factor of either 1.5x or 2.0x


def hitorstand():
    hit = ["hit", "h"]
    stand = ["stand", "s"]
    valid_option = False  # valid when user has provided a valid option
    while not valid_option:
        option = input("Would you like to hit or stand? ").lower()
        if option in hit or option in stand:
            valid_option = option
    if valid_option.startswith("h"):
        print("You chose to hit!")
    else:
        print("You chose to stand!")
    return valid_option


def refresh():  # Refreshes the deck and player's scores. Scores are added to, not calculated per deck.
    # Add the numbered ranks before the special ranks
    global cards
    cards = []
    # Create new cards from the suits and ranks. This is better than hard coding each card
    for i in suits:
        for j in ranks:
            cards.append(j + " of " + i)

    global player, dealer, player_score, dealer_score
    player = []
    dealer = []
    player_score = 0
    dealer_score = 0


def new_round(rounds):  # this function has the main logic of the game
    print("Round " + str(rounds))
    make_bet()
    refresh()
    global player_score, dealer_score, balance
    # Usually, if there are multiple players, the dealer hands out 2 cards to each player before he gets a hidden card.
    player_score += new_card(player)
    dealer_score += new_card(dealer)
    player_score += new_card(player)
    hidden_score = new_card(dealer_hidden)

    print()
    deck_stats(dealer, dealer_score)

    if player_score == 21:  # automatic win.
        balance += (bet * 1.5)
    else:
        while player_score < 21:
            # order is iffy here?
            deck_stats(player, player_score)
            if hitorstand().startswith("s"):  # choosing to stand. break the loop
                break
            else:
                player_score += new_card(player)
        if player_score > 21:
            print("You have busted! You lost this round.")
            return
        dealer.append(dealer_hidden.pop(0))
        print("The dealer has revealed their hidden card.")
        dealer_score += hidden_score
        deck_stats(dealer, dealer_score)
        while dealer_score <= 16:  # dealer must stay with their hand if the value is 17+. else, keep drawing
            dealer_score += new_card(dealer)
            deck_stats(dealer, dealer_score)
        if dealer_score > 21:
            print("The dealer has busted! You win twice your bet.")
            balance += (bet * 2)
        else:
            if player_score > dealer_score:
                # @TODO Make sure the print formatting works in repl.it
                print(
                    "You have won the round! Your deck totaled up to {} and was higher than the dealer's score, {}!".format(
                        player_score, dealer_score))
                balance += (bet * 2)
            else:
                print(
                    "You have lost the round. Your deck totaled up to {} and was not higher than the dealer's score, "
                    "{}.".format(
                        player_score, dealer_score))


def new_card(deck):  # Add a new card to the deck and return its value.
    index = random.randint(0, len(cards) - 1)  # random card.
    card = cards.pop(index)
    deck.append(card)

    card_info = card.split(" of ")  # will split into [value, suit]
    rank_index = ranks.index(card_info[0])
    value = rank_values[rank_index]
    # the index of the card in the ranks corresponds with it's value in the second list, value
    if deck == player:
        print("You have drawn a new card: " + card)
        if value == 11:  # Choose the new value of an Ace.
            # This selection is made on the inside because the print needs to occur.
            ace_value = -1
            while ace_value == -1:
                option = input("Choose the value of an Ace (1 or 11): ")
                if option == "1":
                    ace_value = 1
                elif option == "11":
                    ace_value = 11
    else:
        if value == 11:
            if dealer_score + 11 > 21:
                value = 1
            # Else, it can be 11, and that already is the set default value
    return value


def deck_stats(deck, score):  # prints out the current deck of either the player or dealer and also prints the score
    prefix = "Your"
    if deck == dealer:
        prefix = "Dealer's"
    print(prefix + " current deck: ", end="")
    print(deck)
    print("{} current deck value: {}\n".format(prefix, str(score)))


def main():
    rounds = 0  # rounds elapsed
    while True:
        if balance > 0:  # able to go on if you have money to bet
            new_round(rounds)
            rounds += 1
            if balance > 0:
                keep_going = input("Would you like to keep going? ")
                if not keep_going.lower().startswith("y"):
                    break  # user has chosen to manually end the game
        elif balance <= 0:
            print("You have an invalid balance!")
            break
    print("GG! The game of Blackjack has ended. You ended with: $" + str(balance))


if __name__ == "__main__":
    main()

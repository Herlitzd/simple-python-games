#! /usr/bin/python3


import random
suits = ["♤", "♡", "♧", "♢"]
card_in_suit = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

deck = []


class Card:
    def __init__(self, suit, label):
        self.suit = suit
        self.label = label

    def __repr__(self):
        return "|"+self.suit+str(self.label)+"|"


class Hand:
    def __init__(self):
        self.cards = []
        self.face_down = None

    def add_card(self, card):
        self.cards.append(card)

    def add_card_face_down(self, card):
        self.face_down = card

    def flip(self):
        if self.face_down != None:
            self.cards.append(self.face_down)
            self.face_down = None

    def __repr__(self):
        base = ""
        if self.face_down:
            base += '|??|'
        for card in self.cards:
            base = base + str(card)

        base = base + " @ " + str(self.total())
        return base

    def total(self):
        total = 0
        for card in self.cards:
            if type(card.label) is int:
                total = total + card.label
            else:
                if(card.label == "A"):
                    total = total + 1
                else:
                    total = total + 10

        aces = self.cards.count("A")
        for _ace in range(aces):
            if total + 10 < 21:
                total = total + 10
        return total


games = 0
player_wins = 0
draws = 0
while True:
    print("Wins/Loss/Draw/Total: "+str(player_wins)+" / " +
          str(games-player_wins-draws)+" / "+str(draws)+" / "+str(games))

    for suit in suits:
        for card_label in card_in_suit:
            deck.append(Card(suit, card_label))

    random.shuffle(deck)

    dealer = Hand()
    player = Hand()

    player.add_card(deck.pop())
    dealer.add_card_face_down(deck.pop())
    player.add_card(deck.pop())
    dealer.add_card(deck.pop())

    def print_game():
        print("Dealer", dealer)
        print("Player", player)
        print("\n")

    while(player.total() < 21):
        print_game()
        play = input("h or s: ")
        print("\n")
        if play == "h":
            player.add_card(deck.pop())
        else:
            break

    dealer.flip()

    while(dealer.total() < 17):
        dealer.add_card(deck.pop())
        print_game()

    print("\n\n")
    print_game()
    games = games + 1

    if player.total() > 21 and dealer.total() > 21:
        draws += 1
        print("draw")
    elif player.total() == dealer.total():
        draws += 1
        print("draw")
    elif player.total() <= 21 and dealer.total() > 21:
        player_wins += 1
        print("player wins")
    elif dealer.total() <= 21 and player.total() > 21:
        print("dealer wins")
    elif player.total() > dealer.total():
        player_wins += 1
        print("player wins")
    else:
        print("dealer wins")
    print("\n\n")

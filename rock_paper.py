#! /usr/bin/python3
from random import randint

plays = dict(r="rock", s="scissor", p="paper")

# We need a list of all of the values in our dictionary for the computer move
# above, it is `key=value`, the value being the right hand side of the `=`
plays_as_list = list(plays.values())


def winner(user, computer):
    if(user == computer):
        print("draw, go again")
    elif(user == "rock" and computer == "scissor"):
        print("player wins")
    elif(user == "paper" and computer == "rock"):
        print("player wins")
    elif(user == "scissor" and computer == "paper"):
        print("player wins")
    else:
        print("computer wins")


while True:
    # Get a random number between 0 and 2 (inclusive)
    random_int = randint(0, 2)
    # The computer just picks a random value from
    # the possible plays
    computer_play = plays_as_list[random_int]

    # As the player for a play
    play_letter = input("pick a play: r,p,s: ")
    # Lookup the letter the player gave us in the dictionary
    # so we can get the full value (not just the first letter)
    player_play = plays.get(play_letter)

    print("Player: "+player_play)
    print("Computer: "+computer_play)

    # See if there is a winner
    winner(player_play, computer_play)
    print("\n\n")

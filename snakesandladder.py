import time
import random
import sys
import time

SLEEP_BETWEEN_ACTIONS = 1
def welcome_msg():
    msg = """
    Welcome to Snake and Ladder Game.

       Rules:
      1. Initally both the players are at starting position i.e. 0. 
         Take it in turns to roll the dice. 
         Move forward the number of spaces shown on the dice.
      2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
      3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
      4. The first player to get to the FINAL position is the winner.
      5. Hit enter to roll the dice.
    """
    print(msg)


def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Please enter a valid name for first player: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input("Please enter a valid name for second player: ").strip()

    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name

print("single player at start position---------0")    


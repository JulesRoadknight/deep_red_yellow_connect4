import pytest
import sys
import os
from ai import Ai
from board import Board

sys.path.insert(0, os.path.abspath("lib"))

def test_Can_make_a_move():
    class Moves():
        def __init__(self):
            self.legal_moves = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]]

    com = Ai(Moves())
    number = com.move()
    assert number >= 0 and number <= 7





def move(self, player):
    # Connect4 should do this
    # self.show_board()
    # do move
    # while not self.legal_move
    # A call to how we select eg Ai.select_move
    # player_choice = int(input("Make your move: "))
    #
    if player_choice > 7 or player_choice < 1:
            print("Please enter a number from 1-7")
            self.move(player)
    else:
        if self.moves.legal_moves[player_choice-1] == "Full":
            print("That column is full, please choose again.")
            self.move(player)
        else:
            self.game_board.make_move(player, player_choice-1)

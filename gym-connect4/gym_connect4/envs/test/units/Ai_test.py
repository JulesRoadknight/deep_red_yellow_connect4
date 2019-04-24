import pytest
import sys
import os
from ai import Ai
from board import Board

sys.path.insert(0, os.path.abspath("gym-connect4/gym_connect4/envs/lib"))

class Moves():
    def __init__(self):
        self.legal_moves = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]]

def test_Can_make_a_move():

    computer = Ai(Moves())
    number = computer.move()
    assert number >= 0 and number <= 6

def test_can_not_place_in_a_full_collum():

    class Moves():
        def __init__(self):
            self.legal_moves = ["Full",[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]]
    move_array = [0,1]
    def mock_move():
        return move_array.pop(0)
    computer = Ai(Moves())
    computer.select_move = mock_move
    i = 0
    assert computer.move() == 1

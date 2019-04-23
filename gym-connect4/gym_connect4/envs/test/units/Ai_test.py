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
    assert number >= 0 and number <= 6

import pytest
import sys
import os

sys.path.insert(0, os.path.abspath("gym-connect4/gym_connect4/envs/lib"))
import board

class TestClass:

    def test_new_board(self):
        play_board = board.Board()
        expected_board = [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]]
        assert play_board.show() == expected_board

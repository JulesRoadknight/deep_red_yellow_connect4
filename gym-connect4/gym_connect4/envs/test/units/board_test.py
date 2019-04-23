import pytest
import sys
import os

sys.path.insert(0, os.path.abspath("lib"))

import board

class TestClass:

    def test_new_board(self):
        play_board = board.Board()
        expected_board = [["-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-"]]
        assert play_board.show() == expected_board

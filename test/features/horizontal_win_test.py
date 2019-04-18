import pytest
import sys
import os

sys.path.insert(0, os.path.abspath("lib"))

import connect4 as c4

def test_horizontal_player1_win():
    output = []
    input_values = [1, 5, 2, 5, 3, 5, 4]

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    c4.input = mock_input
    c4.print = lambda s : output.append(s)

    game = c4.Connect4()
    game.start()
    assert output.count("Player 1 wins") == 1

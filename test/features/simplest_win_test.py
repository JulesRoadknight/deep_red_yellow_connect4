import pytest
import sys
import os

sys.path.insert(0, os.path.abspath("lib"))

import connect4 as c4 



def test_simplest_win():
    input_values = [6, 7, 6, 7, 6, 7, 6]
    output = []

    def mock_input(s):
        return input_values.pop(0)

    c4.input = mock_input
    c4.print = lambda s : output.append(s)
    game = c4.Connect4()
    game.start()
    print(output)
    assert output.count("Player 1 wins") == 1
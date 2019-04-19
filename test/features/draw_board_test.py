import pytest
import sys
import os

sys.path.insert(0, os.path.abspath("lib"))

import connect4 as c4

def test_players_draw_the_game():
    output = []
    input_values = [1,2,1,2,1,2,2,1,2,1,2,1,
                    3,4,3,4,3,4,4,3,4,3,4,3,
                    5,6,5,6,5,6,6,5,6,5,6,5,
                    7,7,7,7,7,7]

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    c4.input = mock_input
    c4.print = lambda s : output.append(s)

    game = c4.Connect4()
    game.start()

    assert output.count("It's a Draw!") == 1

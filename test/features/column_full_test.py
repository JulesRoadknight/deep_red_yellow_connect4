import pytest
import sys
import os

sys.path.insert(0, os.path.abspath("lib"))

import connect4 as c4

def test_column_full_handled_again():
    output = []
    input_values = [1,1,1,1,1,1,1,2,3,2,3,2,3,2]

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    c4.input = mock_input
    c4.print = lambda s : output.append(s)

    game = c4.Connect4()
    game.start()

    assert output.count("That column is full, please choose again.") == 1

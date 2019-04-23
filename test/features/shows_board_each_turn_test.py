import pytest
import sys
import os

sys.path.insert(0, os.path.abspath("lib"))

import connect4 as c4

def test_column_full_handled_again():
    output = []
    input_values = [1,2,1,2,1,2,1]

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    c4.input = mock_input
    c4.print = lambda s : output.append(s)

    game = c4.Connect4()
    game.start()

    total = 0
    total += output.count("0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n")
    # total += output.count("The board after the 2nd move")
    total += output.count("0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n1|0|0|0|0|0|0\n")
    total += output.count("0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n1|2|0|0|0|0|0\n")
    total += output.count("0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n1|0|0|0|0|0|0\n1|2|0|0|0|0|0\n")
    total += output.count("0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n1|2|0|0|0|0|0\n1|2|0|0|0|0|0\n")
    total += output.count("0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n1|0|0|0|0|0|0\n1|2|0|0|0|0|0\n1|2|0|0|0|0|0\n")
    total += output.count("0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n1|2|0|0|0|0|0\n1|2|0|0|0|0|0\n1|2|0|0|0|0|0\n")
    total += output.count("0|0|0|0|0|0|0\n0|0|0|0|0|0|0\n1|0|0|0|0|0|0\n1|2|0|0|0|0|0\n1|2|0|0|0|0|0\n1|2|0|0|0|0|0\n")
    assert total == 8

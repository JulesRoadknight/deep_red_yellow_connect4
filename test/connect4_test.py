import pytest
import sys
import os
#0 implies to look at this location first and tells where to look for the modules
#
sys.path.insert(0, os.path.abspath("lib"))

import connect4 as c4 # from connect4 import Connect4

# def test_connect4(c4):

def test_simplest_win():
    input_values = [6, 7, 6, 7, 6, 7, 6]
    output = []

    def mock_input(s):
        return input_values.pop(0)

    c4.Connect4.input = mock_input
    c4.Connect4.print = lambda s : output.append(s)
    c4.Connect4.start()

    assert output.count(["Player 1 wins"]) == 1

def test_c4_start(self):
    mock_board = [["-,-,-,-,-,-,-"],
            ["-,-,-,-,-,-,-"],
            ["-,-,-,-,-,-,-"],
            ["-,-,-,-,-,-,-"],
            ["-,-,-,-,-,-,-"],
            ["-,-,-,-,-,-,-"],
            ["-,-,-,-,-,-,-"]
    ]   
    assert c4.Connect4.start().playing_board == mock_board 
    # assert c4.start.board.playing_board.count == 1 
    # c4.move(1, 6) # c4.move(player, column number)
    # c4.move(2, 7)
    # c4.move(1, 6)
    # c4.move(2, 2)
    # c4.move(1, 6)
    # c4.move(2, 7)
    # assert c4.move(1, 6) == True

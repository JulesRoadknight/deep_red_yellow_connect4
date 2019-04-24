import pytest
import sys
import os
#0 implies to look at this location first and tells where to look for the modules
#
sys.path.insert(0, os.path.abspath("gym-connect4/gym_connect4/envs/lib"))
import connect4 as c4 # from connect4 import Connect4



def test_board_is_empty_when_game_is_initialized():
    game = c4.Connect4()
    output = []
    c4.print = lambda s : output.append(s)
    game.show_board()
    mock_board = "|0||0||0||0||0||0||0|\n|0||0||0||0||0||0||0|\n|0||0||0||0||0||0||0|\n|0||0||0||0||0||0||0|\n|0||0||0||0||0||0||0|\n|0||0||0||0||0||0||0|\n"
    assert  output.count(mock_board) == 1

import pytest
import sys
import os
#0 implies to look at this location first and tells where to look for the modules
#
sys.path.insert(0, os.path.abspath("lib"))

import connect4 as c4 # from connect4 import Connect4



def test_c4_start():
    game = c4.Connect4()
    mock_board = [["-,-,-,-,-,-,-"],
        ["-,-,-,-,-,-,-"],
        ["-,-,-,-,-,-,-"],
        ["-,-,-,-,-,-,-"],
        ["-,-,-,-,-,-,-"],
        ["-,-,-,-,-,-,-"],
        ["-,-,-,-,-,-,-"]
    ]
    assert game.show_board() == mock_board
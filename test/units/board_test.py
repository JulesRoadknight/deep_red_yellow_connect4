import pytest
import sys
import os
#0 implies to look at this location first and tells where to look for the modules
#
sys.path.insert(0, os.path.abspath("lib")

from board import *

def test_new_board():
    play_board = board.Board()
    expected_board = [["-,-,-,-,-,-,-"],
        ["-,-,-,-,-,-,-"],
        ["-,-,-,-,-,-,-"],
        ["-,-,-,-,-,-,-"],
        ["-,-,-,-,-,-,-"],
        ["-,-,-,-,-,-,-"],
        ["-,-,-,-,-,-,-"]
    ]
    assert play_board.show() == expected_board
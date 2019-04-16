import pytest
import sys
#0 implies to look at this location first and tells where to look for the modules
#
sys.path.insert(0, '/Users/student/Documents/Project_Connect4/lib')

from connect4 import Connect4 as c4# from connect4 import Connect4

def test_simplest_win():
    c4.start()
    c4.move(1, 6) # c4.move(player, column number)
    c4.move(2, 7)
    c4.move(1, 6)
    c4.move(2, 2)
    c4.move(1, 6)
    c4.move(2, 7)
    assert c4.move(1, 6) == True

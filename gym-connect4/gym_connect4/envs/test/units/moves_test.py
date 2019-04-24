import pytest
import sys
import os

sys.path.insert(0, os.path.abspath("gym-connect4/gym_connect4/envs/lib"))

import move as module

class TestClass:

    def test_new_move(self):
        move = module.Move()
        assert move.legal_moves == [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]]

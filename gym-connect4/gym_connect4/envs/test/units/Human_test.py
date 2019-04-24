import pytest
import sys
import os
import human
from human import Human

sys.path.insert(0, os.path.abspath("gym-connect4/gym_connect4/envs/lib"))
def test_player_Can_make_a_move():
    output = []
    input_values = ["7"]
    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    human.input = mock_input

    class Moves():
        def __init__(self):
            self.legal_moves = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]]

    hum = Human(Moves())
    number = hum.move()
    assert number >= 0 and number <= 6

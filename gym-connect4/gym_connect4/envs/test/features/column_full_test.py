import pytest
import sys
import os

sys.path.insert(0, os.path.abspath("gym-connect4/gym_connect4/envs/lib"))
print(sys.path)

import connect4 as c4

class TestClass():

    def setup_module():
        pass

    def test_column_full_handled_again(self):
        output = []
        c4_input_values = ["Human", "Human"]
        human_input_values = [1,1,1,1,1,1,1,2,3,2,3,2,3,2]

        def mock_input(s):
            output.append(s)
            return f'{c4_input_values.pop(0)}'

        c4.input = mock_input
        c4.print = lambda s : output.append(s)

        game = c4.Connect4()
        game.test(human_input_values)
        game.start()

        assert output.count("Please make a legal move: ") == 1

    def test_human_makes_two_illegal_moves_is_dealt_with(self):
        output = []
        c4_input_values = ["Human", "Human"]
        human_input_values = [1,1,1,1,1,1,1,1, 2,3,2,3,2,3,2]

        def mock_input(s):
            output.append(s)
            return f'{c4_input_values.pop(0)}'

        c4.input = mock_input
        c4.print = lambda s : output.append(s)

        game = c4.Connect4()
        game.test(human_input_values)
        game.start()

        assert output.count("Please make a legal move: ") == 2
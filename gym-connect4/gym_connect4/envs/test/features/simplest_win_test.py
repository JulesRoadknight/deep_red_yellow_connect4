
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath("gym-connect4/gym_connect4/envs/lib"))
import connect4 as c4

def test_simplest_player1_win():

    output = []
    c4_input_values = ["Human", "Human"]
    human_input_values = [6, 7, 6, 7, 6, 7, 6]

    def mock_input(s):
        output.append(s)
        return f'{c4_input_values.pop(0)}'

    c4.input = mock_input
    c4.print = lambda s : output.append(s)
    game = c4.Connect4()
    game.test(human_input_values)
    game.start()
    assert output.count("Player 1 wins") == 1

def test_simplest_player2_win():

    output = []
    c4_input_values = ["Human", "Human"]
    human_input_values = [6, 7, 6, 7, 6, 7, 5, 7]

    def mock_input(s):

        output.append(s)
        return c4_input_values.pop(0)

    c4.input = mock_input
    c4.print = lambda s : output.append(s)
    game = c4.Connect4()
    game.test(human_input_values)
    game.start()
    assert output.count("Player 2 wins") == 1

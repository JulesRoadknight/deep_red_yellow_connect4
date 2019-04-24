import pytest
import sys
import os

sys.path.insert(0, os.path.abspath("/gym-connect4/gym_connect4/envs/lib"))
import connect4 as c4

def test_diaganol_win_for_player1_from_bottom_left_corner():
    output = []
    c4_input_values = ["Human", "Human"]
    human_input_values = [1,2,2,3,4,3,3,4,4,5,4]

    def mock_input(s):
        output.append(s)
        return f'{c4_input_values.pop(0)}'

    c4.input = mock_input
    c4.print = lambda s : output.append(s)

    game = c4.Connect4()
    game.test(human_input_values)
    game.start()

    assert output.count("Player 1 wins") == 1

def test_diaganol_win_for_player1_from_2nd_collumn_row_2_last_move_in_1_from_top():
    output = []
    c4_input_values = ["Human", "Human"]
    human_input_values = [2,1,2,3,4,3,3,5,5,5,4,5,5,4,4]

    def mock_input(s):
        output.append(s)
        return c4_input_values.pop(0)

    c4.input = mock_input
    c4.print = lambda s : output.append(s)

    game = c4.Connect4()
    game.test(human_input_values)
    game.start()

    assert output.count("Player 1 wins") == 1

def test_diaganol_win_for_player1_from_bottom_left_corner_to_last_move_in_2_from_top_of_diagonal():
    output = []
    c4_input_values = ["Human", "Human"]
    human_input_values = [1, 2, 3, 3, 3, 4, 4, 4, 4, 5, 2]

    def mock_input(s):
        output.append(s)
        return c4_input_values.pop(0)

    c4.input = mock_input
    c4.print = lambda s : output.append(s)

    game = c4.Connect4()
    game.test(human_input_values)
    game.start()

    assert output.count("Player 1 wins") == 1

def test_diaganol_win_for_player1_from_bottom_left_corner_to_middle_last_move_bottom_left():
    output = []
    c4_input_values = ["Human", "Human"]
    human_input_values = [3, 2, 2, 3, 3, 4, 4, 4, 4, 5, 1]

    def mock_input(s):
        output.append(s)
        return c4_input_values.pop(0)

    c4.input = mock_input
    c4.print = lambda s : output.append(s)

    game = c4.Connect4()
    game.test(human_input_values)
    game.start()

    assert output.count("Player 1 wins") == 1

import pytest
import sys
import os

sys.path.insert(0, os.path.abspath("/gym-connect4/gym_connect4/envs/lib"))
import connect4 as c4

def test_diaganol_win_for_player1_from_bottom_right_corner():
    output = []
    input_values = [7,6,6,5,5,4,5,4,4,2,4]

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    c4.input = mock_input
    c4.print = lambda s : output.append(s)

    game = c4.Connect4()
    game.start()

    assert output.count("Player 1 wins") == 1

def test_diaganol_win_for_player1_from_bottom_right_corner_to_middle_with_last_piece_1_from_top():
    output = []
    input_values = [7,6,6,4,5,5,4,4,4,3,5]

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    c4.input = mock_input
    c4.print = lambda s : output.append(s)

    game = c4.Connect4()
    game.start()

    assert output.count("Player 1 wins") == 1

def test_diaganol_win_for_player1_from_bottom_right_corner_to_middle_with_last_piece_2_from_top():
    output = []
    input_values = [7, 6, 5, 5, 5, 4, 4, 4, 4, 3, 6]

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    c4.input = mock_input
    c4.print = lambda s : output.append(s)

    game = c4.Connect4()
    game.start()

    assert output.count("Player 1 wins") == 1

def test_diaganol_win_for_player1_from_bottom_right_corner_to_middle_with_last_piece_at_bottom():
    output = []
    input_values = [5, 6, 6, 5, 5, 4, 4, 4, 4, 3, 7]

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    c4.input = mock_input
    c4.print = lambda s : output.append(s)

    game = c4.Connect4()
    game.start()

    assert output.count("Player 1 wins") == 1

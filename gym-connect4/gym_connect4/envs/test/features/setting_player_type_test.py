import pytest
import sys
import os
import connect4 as c4

sys.path.insert(0, os.path.abspath("gym-connect4/gym_connect4/envs/lib"))

def test_players_are_set_to_ai_vs_ai():

    output = []
    c4_input_values = ["AI", "AI"]
    human_input_values = [1,1,1,1]

    def mock_input(s):
        output.append(s)
        return f'{c4_input_values.pop(0)}'

    c4.input = mock_input
    c4.print = lambda s : output.append(s)

    game = c4.Connect4()
    game.test(human_input_values)
    game.start()

    total = 0
    total += output.count("Player 1 is a Human or AI?")
    total += output.count("Player 2 is a Human or AI?")

    assert total == 2

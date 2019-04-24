import sys
import numpy as np
from connect4 import Connect4
import board

sys.path.append('..')

# from Game import Game
# from .Connect4Logic import Board

class Connect4Game(Connect4):
    #implements the alpha-zero-general Game interface

    def __init__(self, height=0, width=0, win_length=0, np_pieces=0):
        Connect4.__init__(self)
        self.base_board = board.Board()
        # print(self.base_board)
        self.base_board_height = len(self.base_board.show())
        print("This is the game board height:")
        print(self.base_board_height)
        self.base_board_width = len(self.base_board.show()[0])
        print("This is the game board width:")
        print(self.base_board_width)
        # print(self.base_board.game_board[0])
        # print("This is the board height:")
        # print(self.base_board_height)
        # self.base_board_width = len(self.base_board.game_board[0][0])
        # print("This is the board width:")
        # print(self.base_board_width)
        # self.base_board_win_length = win_length
        self.base_board_np_pieces = np_pieces

    def getInitBoard(self):
        return True

c4 = Connect4Game(Connect4)
print(c4)

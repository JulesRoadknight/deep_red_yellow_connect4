import sys
import numpy as np
sys.path.append('../alpha-zero-general/')
from Game import Game
sys.path.append('../gym-connect4/gym_connect4/envs/lib/')
from board import Board
import move


class Connect4Game(Game):
    #implements the alpha-zero-general Game interface

    def __init__(self):
        print("init")
        Game.__init__(self)
        self._base_board = Board()

    def _playBoard(self, board):
        b = Board()
        player = None
        for w in range(0, len(board[0])):
            for h in range(0, len(board)):
                value = board[h][w]
                if not b.moves.check_win() and value != 0:
                    b.make_move(value, w)
                    player = value
        return (b, player)

    def getInitBoard(self):
        print("getInitBoard")
        return np.array(self._base_board.show())

    def getBoardSize(self):
        print("getBoardSize")
        return (len(self._base_board.show()), len(self._base_board.show()[0]))

    def getActionSize(self):
        print("getActionSize")
        return len(self._base_board.show()[0])

    def getNextState(self, board, player, action):
        print("getNextState")
        print(action)
        b = self._playBoard(board)[0]
        b.make_move(player, action)
        return np.array(b.show()), -player

    def getValidMoves(self, board, player):
        print("getValidMoves")
        "Any zero value in top row in a valid move"
        b = self._playBoard(board)[0]
        return np.array(b.show())[0] == 0

    def getGameEnded(self, board, player):
        print("getGameEnded")
        (b, winning_player) = self._playBoard(board)

        if b.moves.check_win():
            if winning_player == player:
                return +1
            elif winning_player == -player:
                return -1
        else:
            # 0 used to represent unfinished game.
            return 0

    def getCanonicalForm(self, board, player):
        # Flip player from 1 to -1
        print("getCanonicalForm")
        return board * player

    def getSymmetries(self, board, pi):
        print("getSymmetries")
        """Board is left/right board symmetric"""
        return [(np.array(board), pi), (np.array(board)[:, ::-1], pi[::-1])]

    def stringRepresentation(self, board):
        b = self._playBoard(board)
        return str(b)

def display(board):
    print(" -----------------------")
    print(' '.join(map(str, range(len(board[0])))))
    print(board)
    print(" -----------------------")

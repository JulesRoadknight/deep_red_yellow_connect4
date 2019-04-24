import sys
import numpy as np
sys.path.append('../alpha-zero-general/')
from Game import Game
sys.path.append('../gym-connect4/gym_connect4/envs/lib/')
import board
import move


class Connect4Game(Game):
    #implements the alpha-zero-general Game interface

    def __init__(self):
        Game.__init__(self)
        self._base_board = board.Board()

    def _playBoard(self, board):
        b = board.Board()
        (m, n) = b.show().shape
        player = None
        for w in range(0, n):
            for h in range(0, m):
                value = board[h][w]
                if not b.moves.check_win() and value != 0:
                    b.make_move(value, w)
                    player = value

        return (b, player)

    def getInitBoard(self):
        return self._base_board

    def getBoardSize(self):
        return (len(self._base_board.show()), len(self._base_board.show()[0]))

    def getActionSize(self):
        return len(self._base_board.show()[0])

    def getNextState(self, board, player, action):
        b = self._playBoard(board)[0]
        b.make_move(player, action)
        return (b.game_board, -player)

    def getValidMoves(self, board, player):
        "Any zero value in top row in a valid move"
        return self._base_board[0] == 0

    def getGameEnded(self, board, player):
        (b, winning_player) = self._playBoard(board)

        if b.moves.check_win():
            if winning_player == player:
                return +1
            elif winning_player == -player:
                return -1
            else:
                raise ValueError('Unexpected winstate found: ', winstate)
        else:
            # 0 used to represent unfinished game.
            return 0

    def getCanonicalForm(self, board, player):
        # Flip player from 1 to -1
        return board * player

    def getSymmetries(self, board, pi):
        """Board is left/right board symmetric"""
        return [(board, pi), (board[:, ::-1], pi[::-1])]

    def stringRepresentation(self, board):
        b = self._playBoard(board)
        return str(b)

def display(board):
    print(" -----------------------")
    print(' '.join(map(str, range(len(board[0])))))
    print(board)
    print(" -----------------------")

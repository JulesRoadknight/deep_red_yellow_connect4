import os
import sys
import numpy as np
from Connect4Game import Connect4Game as Game
sys.path.insert(0, os.path.abspath('../alpha-zero-general/'))
from MCTS import MCTS
from utils import dotdict
from connect4.tensorflow.NNet import NNetWrapper as NNet

class AlphaZeroAI():

    def __init__(self, board=None, player=1):
        self.g = Game()
        self.n1 = NNet(self.g)
        self.n1.load_checkpoint(os.getcwd() + '/model/','connect4.pth.tar')
        self.args1 = dotdict({'numMCTSSims': 25, 'cpuct':1.0})
        self.mcts1 = MCTS(self.g, self.n1, self.args1)
        self.n1p = lambda x: np.argmax(self.mcts1.getActionProb(x, temp=0))
        self.board = board
        self.moves = self.board.moves
        if player == 1:
            self.player = 1
        if player == 2: 
            self.player = -1   

    def move(self):
        choice = self.select_move()
        while not self.legal(choice):
            choice = self.select_move()
        return choice

    def select_move(self):
        action = self.n1p(self.g.getCanonicalForm(np.array(self.board.show()), self.player))
        print('AI move: {0}'.format(action+1))
        return action

    def legal(self, choice):
        if self.moves.legal_moves[choice] == "Full":
            return False
        return True
      
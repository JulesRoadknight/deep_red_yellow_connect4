import gym, os, sys
from gym import error, spaces, utils
from gym.utils import seeding
import random
print(sys.path.insert(0, os.path.abspath("gym-connect4/gym_connect4/envs/lib")))
print(sys.path)
from connect4 import Connect4
class Connect4Env(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.action_space = spaces.Discrete(7)
        self.observation_space = spaces.Box(0,2,(7,6))

    def step(self, action):
        self.game.move(1,random.randint(0,6))
        board = self.game.game_board
        if self.game.gameover():
            reward = -40
            return board, reward, self.game.gameover()
        self.game.move(2, action)
        board = self.game.game_board
        if self.game.gameover():
            reward = 50
            return board, reward, self.game.gameover()
        reward = 0
        return board, reward, self.game.gameover()

    def reset(self):
        self.game = Connect4()

    def render(self):
        pass
    def close(self):
        pass

import gym
from gym import error, spaces, utils
from gym.utils import seeding

class ConnectEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        ...
    def step(self, action):
        ...
    def reset(self):
        ...
    def close(self):
        ...

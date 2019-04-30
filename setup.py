import os
import sys
sys.path.insert(0, os.path.abspath('gym-connect4/gym_connect4/envs/lib'))
import connect4 as c4

game = c4.Connect4()

game.start()

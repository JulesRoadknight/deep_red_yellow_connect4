In the console, run:

python

import os
import sys
sys.path.insert(0, os.path.abspath('lib'))
import connect4 as c4

game = c4.Connect4()

game.start()


  Then, type numbers 0-6 to make moves, alternating between players.

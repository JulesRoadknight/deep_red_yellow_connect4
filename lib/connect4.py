class Connect4():

    def __init__(self):
        self.playing_board = [["-,-,-,-,-,-,-"],
            ["-,-,-,-,-,-,-"],
            ["-,-,-,-,-,-,-"],
            ["-,-,-,-,-,-,-"],
            ["-,-,-,-,-,-,-"],
            ["-,-,-,-,-,-,-"],
            ["-,-,-,-,-,-,-"]
    ]  

    def start(self):
        return self.playing_board

    def move(self, player, column):
        print('Enter your move: ')
        column = input()
        return True
# comment for commit

c4 = Connect4()
c4.start()
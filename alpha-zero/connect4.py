import sys
from AlphaZeroAI import AlphaZeroAI as AI
sys.path.append('../gym-connect4/gym_connect4/envs/lib/')
import board
import move
import human

class Connect4():

    def __init__(self):
        self.game_board = board.Board()
        self.moves = self.game_board.moves
        self.player1 = AI(self.game_board, 1)
        self.player2 = AI(self.game_board, 2)

    def test(self, input_values):
        def mock_input(s):
            print(s)
            return input_values.pop(0)
        human.input = mock_input

    def start(self):
        self.players()
        player = 2
        not_over = True
        turn = 1
        while not_over and turn <= 42 :
            if player == 1 :
                player = 2
                self.game_board.make_move(1, self.player1.move())
            else:
                player = 1
                self.game_board.make_move(-1, self.player2.move())
            self.show_board()
            not_over = not self.gameover()
            turn += 1

        if not_over == True:
            print("It's a Draw!")
        else:
            self.show_board()
            if player == 1 :
                print('Player 2 wins')
            else:
                print('Player 1 wins')
                
    def show_board(self):
        string = ""
        i = len(self.game_board.game_board)-1
        while i > -1:
            row = self.game_board.game_board[i]
            for token in row:
                if token == 1:
                    string +=  '|1|'
                elif token == -1:
                    string +=  '|2|'
                else:
                    string +=  '|0|'        
                
            string += "\n"
            i -= 1
        print(string)

    def gameover(self):
        return self.game_board.moves.check_win()

    def players(self):
        if raw_input("Player 1 is a Human or AI?") == "Human" : self.player1 = human.Human(self.moves)   
        if raw_input("Player 1 is a Human or AI?") == "Human" : self.player2 = human.Human(self.moves)
        return

if __name__ == "__main__":
    c4 = Connect4()
    c4.start()        

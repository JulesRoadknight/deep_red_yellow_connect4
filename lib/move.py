class Move():
    def __init__(self):
        self.legal_moves = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]]
        self.player1 = []
        self.player2 = []

    def add_legal_move(self, coords):
        self.legal_moves.insert(coords[0], coords)

    def save_move(self, player, legal_move_index):
        self.player = player
        if player == 1:
            move = self.legal_moves.pop(legal_move_index)
            self.player1.insert(0, move)
            self.legal_moves.insert(legal_move_index, [move[0],move[1]+1])

        else :
            move = self.legal_moves.pop(legal_move_index)
            self.player2.insert(0, move)
            self.legal_moves.insert(legal_move_index, [move[0],move[1]+1])
        return move

    def check_win(self):
        if len(self.player1) > 3 :
            return self.check_vertical() or self.check_horizontal()
        return False

    def check_vertical(self):
        array = []
        total = 0
        if self.player == 1 and len(self.player1) > 3:
            for coords in self.player1:
                if coords[1] != 3 : continue
                valid_coord = coords[0]
                for co_ord in self.player1:
                    if valid_coord == co_ord[0] : array.append(co_ord)
        elif self.player == 2 and len(self.player2) > 3:
            for coords in self.player2:
                if coords[1] != 3 : continue
                valid_coord = coords[0]
                for co_ord in self.player2:
                    if valid_coord == co_ord[0] : array.append(co_ord)
        for coords in array:
            total += coords[1]

        if total == 6 or total == 10 or total == 14:
            return True
        else:
            return False

    def check_horizontal(self):
        array = []
        if self.player == 1:
            last_move = self.player1[0]
            for coords in self.player1:
                if coords[1] == last_move[1]: array.append(coords)
        else:
            last_move = self.player2[0]
            for coords in self.player2:
                if coords[1] == last_move[1]: array.append(coords)

        if array.count([0,last_move[1]]) == 1 and array.count([1,last_move[1]]) == 1 and array.count([2,last_move[1]]) == 1 and array.count([3,last_move[1]]) == 1:
            return True
        if array.count([1,last_move[1]]) == 1 and array.count([2,last_move[1]]) == 1 and array.count([3,last_move[1]]) == 1 and array.count([4,last_move[1]]) == 1:
            return True
        if array.count([2,last_move[1]]) == 1 and array.count([3,last_move[1]]) == 1 and array.count([4,last_move[1]]) == 1 and array.count([5,last_move[1]]) == 1:
            return True
        if array.count([3,last_move[1]]) == 1 and array.count([4,last_move[1]]) == 1 and array.count([5,last_move[1]]) == 1 and array.count([6,last_move[1]]) == 1:
            return True
        return False

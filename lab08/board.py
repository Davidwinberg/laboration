class TicTacToeBoard:
    def __init__(self):
        self._board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


    def get(self, row, column):
        return self._board[row][column]


    def is_empty(self, row, column):
        if self._board[row][column] == "-":
            return True
        else:
            return False


    def place(self, marker, row, column):
        if self._board[row][column] == "-":
            self._board[row][column] = marker
            return True
        else:
            return False


    def is_full(self):
        for row in self._board:
            for x in row:
                if x == "-":
                    return False
        return True


    def is_winner(self, marker):
        b = self._board
        # Column
        if b[0][0] == marker and b[1][0] == marker and b[2][0] == marker:
            return print(1), True

        elif b[0][1] == marker and b[1][1] == marker and b[2][1] == marker:
            return print(2), True

        elif b[0][2] == marker and b[1][2] == marker and b[2][2] == marker:
            return print(3), True

        # Row
        for row in b:
            if row[0] == row[1] and row[1] == row[2] and row[2] == marker:
                return print(4), True

        # Diagonal
        if b[0][0] == marker and b[1][1] == marker and b[2][2] == marker:
            return print(5), True

        elif b[0][2] == marker and b[1][1] == marker and b[2][0] == marker:
            return print(6), True

        return False



    def restart(self):
        self._board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


if __name__ == '__main__':
    print("Hello world")


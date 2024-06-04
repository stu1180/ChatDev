'''
This file contains the Board class which represents the game board.
'''
class Board:
    def __init__(self, size=15):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
    def is_valid_move(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size and self.grid[row][col] == ' '
    def place_piece(self, row, col, symbol):
        if self.is_valid_move(row, col):
            self.grid[row][col] = symbol
            return True
        return False
    def is_full(self):
        for row in self.grid:
            if ' ' in row:
                return False
        return True
    def has_winning_sequence(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] != ' ' and self._has_winning_sequence_at(i, j):
                    return True
        return False
    def _has_winning_sequence_at(self, row, col):
        symbol = self.grid[row][col]
        # Check horizontal
        if col + 4 < self.size and all(self.grid[row][col+k] == symbol for k in range(5)):
            return True
        # Check vertical
        if row + 4 < self.size and all(self.grid[row+k][col] == symbol for k in range(5)):
            return True
        # Check diagonal (top-left to bottom-right)
        if row + 4 < self.size and col + 4 < self.size and all(self.grid[row+k][col+k] == symbol for k in range(5)):
            return True
        # Check diagonal (top-right to bottom-left)
        if row + 4 < self.size and col - 4 >= 0 and all(self.grid[row+k][col-k] == symbol for k in range(5)):
            return True
        return False
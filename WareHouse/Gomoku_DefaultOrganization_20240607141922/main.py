'''
This is the main file of the Gomoku game. It initializes the game and starts the GUI.
'''
import tkinter as tk
import tkinter.messagebox as messagebox
from game import Game
from board import Board
from player import Player
class GomokuApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gomoku")
        self.board = Board()
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")
        self.game = Game(self.board, self.player1, self.player2)
        self.create_board()
    def create_board(self):
        self.buttons = []
        for i in range(self.board.size):
            row = []
            for j in range(self.board.size):
                button = tk.Button(self.master, text="", width=2, height=1,
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
    def make_move(self, row, col):
        if self.game.is_game_over():
            return
        player = self.game.get_current_player()
        if self.game.make_move(row, col):
            self.buttons[row][col].config(text=player.symbol)
            if self.game.is_game_over():
                winner = self.game.get_winner()
                if winner:
                    messagebox.showinfo("Game Over", f"{winner.name} wins!")
                else:
                    messagebox.showinfo("Game Over", "It's a draw!")
        else:
            messagebox.showerror("Invalid Move", "This cell is already occupied.")
    def start(self):
        self.master.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    app = GomokuApp(root)
    app.start()
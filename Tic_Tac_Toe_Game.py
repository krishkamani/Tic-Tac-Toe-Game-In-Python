from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        self.a = 1
        self.b = 0
        self.c = 0

        self.create_widgets()

    def create_widgets(self):
        # Add Buttons
        self.buttons = [ttk.Button(self.master, text=' ') for _ in range(9)]
        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col, sticky='snew', ipadx=40, ipady=40)
            button.config(command=lambda i=i: self.button_click(i + 1))

        self.player_turn_label = ttk.Label(self.master, text="   Player 1 turn!   ")
        self.player_turn_label.grid(row=3, column=0, sticky='snew', ipadx=40, ipady=40)

        self.player_details_label = ttk.Label(self.master, text="    Player 1 is X\n\n    Player 2 is O")
        self.player_details_label.grid(row=3, column=2, sticky='snew', ipadx=40, ipady=40)

        self.restart_button = ttk.Button(self.master, text='Restart', command=self.restart_button)
        self.restart_button.grid(row=3, column=1, sticky='snew', ipadx=40, ipady=40)

    def restart_button(self):
        self.a = 1
        self.b = 0
        self.c = 0
        self.player_turn_label['text'] = "   Player 1 turn!   "
        for button in self.buttons:
            button['text'] = ' '
            button.state(['!disabled'])

    def disable_buttons(self):
        for button in self.buttons:
            button.state(['disabled'])

    def button_click(self, id):
        print("ID:{}".format(id))

        if ' ' not in [button['text'] for button in self.buttons]:
            tkinter.messagebox.showinfo("Tic Tac Toe", "Match is Draw.")
            self.disable_buttons()
            self.c = 1
            return

        player = "Player 1" if self.a == 1 else "Player 2"
        if self.buttons[id - 1]['text'] == ' ':
            self.buttons[id - 1]['text'] = "X" if self.a == 1 else "O"
            self.a = 1 - self.a
            self.b += 1

            if self.check_winner():
                self.disable_buttons()
                self.c = 1
                tkinter.messagebox.showinfo("Tic Tac Toe", f"Winner is {player}")

            if self.a == 1 and self.c == 0:
                self.player_turn_label['text'] = "   Player 1 turn!   "
            elif self.a == 0 and self.c == 0:
                self.player_turn_label['text'] = "   Player 2 turn!   "

    def check_winner(self):
        winning_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        for condition in winning_conditions:
            if self.buttons[condition[0]]['text'] == self.buttons[condition[1]]['text'] == self.buttons[condition[2]]['text'] != ' ':
                return True

        return False

if __name__ == "__main__":
    root = Tk()
    game = TicTacToe(root)
    root.mainloop()

from tkinter import *
from tkinter import ttk
import tkinter.messagebox


def make_button(id):
    button = ttk.Button(root, text=' ')
    button.grid(row=id // 3, column=id % 3, sticky='snew', ipadx=40, ipady=40)
    button.config(command=lambda: ButtonClick(id + 1))
    buttons.append(button)


root = Tk()
buttons = []
root.title("Tic Tac Toe")
# add Buttons
for i in range(9):
    make_button(buttons, i)

playerturn = ttk.Label(root, text="   Player 1 turn!  ")
playerturn.grid(row=3, column=0, sticky='snew', ipadx=40, ipady=40)

playerdetails = ttk.Label(root, text="    Player 1 is X\n\n    Player 2 is O")
playerdetails.grid(row=3, column=2, sticky='snew', ipadx=40, ipady=40)

res = ttk.Button(root, text='Restart')
res.grid(row=3, column=1, sticky='snew', ipadx=40, ipady=40)
res.config(command=lambda: restartbutton())

a = 1
b = 0
c = 0


def restartbutton():
    global a, b, c
    a = 1
    b = 0
    c = 0
    playerturn['text'] = "   Player 1 turn!   "
    for button in buttons:
        button['text'] = ' '
        button.state(['!disabled'])


# after getting result(win or loss or draw) disable button
def disableButton():
    for button in buttons:
        button.state(['disabled'])


def ButtonClick(id):
    global a, b, c
    print("ID:{}".format(id))
    i = id - 1
    # for player 1 turn
    if buttons[i]['text'] == ' ':
        buttons[i]['text'] = "X" if a == 1 else "O"
        a = 1 - a
        b += 1


    # checking for winner
    if (buttons[0]['text'] == 'X' and buttons[1]['text'] == 'X' and buttons[2]['text'] == 'X' or
            buttons[3]['text'] == 'X' and buttons[4]['text'] == 'X' and buttons[5]['text'] == 'X' or
            buttons[6]['text'] == 'X' and buttons[7]['text'] == 'X' and buttons[8]['text'] == 'X' or
            buttons[0]['text'] == 'X' and buttons[3]['text'] == 'X' and buttons[6]['text'] == 'X' or
            buttons[1]['text'] == 'X' and buttons[4]['text'] == 'X' and buttons[7]['text'] == 'X' or
            buttons[2]['text'] == 'X' and buttons[5]['text'] == 'X' and buttons[8]['text'] == 'X' or
            buttons[0]['text'] == 'X' and buttons[4]['text'] == 'X' and buttons[8]['text'] == 'X' or
            buttons[2]['text'] == 'X' and buttons[4]['text'] == 'X' and buttons[6]['text'] == 'X'):
        disableButton()
        c = 1
        tkinter.messagebox.showinfo("Tic Tac Toe", "Winner is player 1")
    elif (buttons[0]['text'] == 'O' and buttons[1]['text'] == 'O' and buttons[2]['text'] == 'O' or
          buttons[3]['text'] == 'O' and buttons[4]['text'] == 'O' and buttons[5]['text'] == 'O' or
          buttons[6]['text'] == 'O' and buttons[7]['text'] == 'O' and buttons[8]['text'] == 'O' or
          buttons[0]['text'] == 'O' and buttons[3]['text'] == 'O' and buttons[6]['text'] == 'O' or
          buttons[1]['text'] == 'O' and buttons[4]['text'] == 'O' and buttons[7]['text'] == 'O' or
          buttons[2]['text'] == 'O' and buttons[5]['text'] == 'O' and buttons[8]['text'] == 'O' or
          buttons[0]['text'] == 'O' and buttons[4]['text'] == 'O' and buttons[8]['text'] == 'O' or
          buttons[2]['text'] == 'O' and buttons[4]['text'] == 'O' and buttons[6]['text'] == 'O'):
        disableButton()
        c = 1
        tkinter.messagebox.showinfo("Tic Tac Toe", "Winner is player 2")
    elif b == 9:
        disableButton()
        c = 1
        tkinter.messagebox.showinfo("Tic Tac Toe", "Match is Draw.")

    if a == 1 and c == 0:
        playerturn['text'] = "   Player 1 turn!   "
    elif a == 0 and c == 0:
        playerturn['text'] = "   Player 2 turn!   "


root.mainloop()

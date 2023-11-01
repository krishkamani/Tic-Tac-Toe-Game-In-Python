#Import the sockets library
import socket
import threading
import gameboard as gb

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

#Define my socket address information
serverAddress = None
serverPort = None

#create a socket object on my server
connectionSocket = None

start = False
user = False
player1 = ""
board = None
pos = 0
finish = False
username = ""
isCon = False
close = False

def createThread(con):
    thread = threading.Thread(target=con)
    thread.daemon = True
    thread.start()


def receiveMove():
    global pos,start,user
    while True:  
        if isCon and start and user:
            try:
                data,addr = connectionSocket.recvfrom(1024)
                data = data.decode()
                print(data)    
                if data != "":     
                    pos,board.lastMove = data.split("-")
                    board.playMoveOnBoard(int(pos),board.lastMove)
                    updateBoard()
                    lblTurn["text"] = "You"
                    play()
            except:
                lblTurn["text"] = "you"
                pass
        

def receive():
    global start,user,board,username,player1,connectionSocket,isCon,close
    while True:
        if isCon:
            if (not start or not user):
                data,addr = connectionSocket.recvfrom(1024)
                data = data.decode()
                print(data)
                if data == "Not accepted":
                    isCon = True
                    connectionSocket.close()
                elif data == "accepted":
                    username = simpledialog.askstring("Input", "Enter your name?",parent=window)
                    #username = "maneesha"
                    sendData = '{}'.format(username).encode()
                    connectionSocket.send(sendData)
                    lblUsername["text"] = username
                    print(sendData)
                    start = True   
                    close = False            
                elif data == "player1": 
                    player1 = data              
                    board = gb.Board(username)
                    board.lastMove = player1
                    user = True
                    break


def clickConnect():
    global serverAddress,serverPort,connectionSocket,isCon
    if not isCon:
        serverAddress = simpledialog.askstring("Input", "What is host name/ip address?",parent=window)
        serverPort = simpledialog.askstring("Input", "What is the port?",parent=window)
        if serverAddress != "" and serverPort != "":
            try:
                connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                connectionSocket.connect((serverAddress,int(serverPort)))
                isCon = True
                lblTurn["text"] = "You"
                lblGames["text"] = " "
                lblWon["text"] = " "
                lblLost["text"] = " "
                lblTies["text"] = " "
                lblUsername["text"] = " "
                try:
                    receive()
                except Exception:
                    isCon = False
                    messagebox.showerror("Error", "Host rejected to connect!")
            except Exception:
                messagebox.showerror("Error", "Invalid hostname or port!")
        else:
            messagebox.showerror("Error", "Invalid hostname or port!")
 

def clickQuit():
    if start or user:
        connectionSocket.close()
    window.destroy()


createThread(receiveMove)


window=Tk()
window.title("TiC-Tac-Toe Player2")
window.geometry("930x650+0+0")
window.resizable(width=False, height=False)
window.configure(background = 'Cadet Blue')

tops = Frame(window, bg ='Cadet Blue', pady =2, width = 1350, height=100, relief = RIDGE)
tops.grid(row=0, column =0)

lblTitle = Label(tops, font=('arial',50,'bold'),text="Tic Tac Toe Game", bd=21, bg='Cadet Blue',fg='Cornsilk',justify = CENTER)
lblTitle.grid(row=0,column = 0)

mainFrame = Frame (window, bg = 'Powder Blue', bd=10,width = 1350, height=600, relief=RIDGE) 
mainFrame.grid(row=1,column=0)

leftFrame = Frame (mainFrame ,bd=10, width =750, height=500, pady=2, padx=10, bg="Cadet Blue", relief=RIDGE)
leftFrame.pack(side=LEFT)

rightFrame = Frame (mainFrame,bd=10, width =560, height=500, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE)
rightFrame.pack(side=RIGHT)

rightFrame1=Frame(rightFrame ,bd=10, width=560, height=200, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE) 
rightFrame1.grid(row=0, column=0)

rightFrame2 = Frame(rightFrame,bd=10, width =560, height=250, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE)
rightFrame2.grid(row=1,column=0)

rightFrame3=Frame(rightFrame ,bd=10, width=560, height=150, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE) 
rightFrame3.grid(row=2, column=0)



def clicked1():
    global finish,board
    if start and user and btn1["text"]==" ":   #For getting the text of a button
        if board.lastMove == player1:
            btn1["text"]="X"
            board.lastMove = username
            sendData = '{}-{}'.format("0",board.lastMove).encode()
            connectionSocket.send(sendData)
            board.playMoveOnBoard(0,board.lastMove)
            lblTurn["text"] = "opponent"
            print(sendData)   
            play()
        
def clicked2():
    global finish,board
    if start and user and btn2["text"]==" ":   #For getting the text of a button
        if board.lastMove == player1:
            btn2["text"]="X"
            board.lastMove = username
            sendData = '{}-{}'.format("1",board.lastMove).encode()
            connectionSocket.send(sendData)
            board.playMoveOnBoard(1,board.lastMove)
            lblTurn["text"] = "opponent"
            print(sendData)    
            play()

def clicked3():
    global finish,board
    if start and user and btn3["text"]==" ":   #For getting the text of a button
        if board.lastMove == player1:
            btn3["text"]="X"
            board.lastMove = username
            sendData = '{}-{}'.format("2",board.lastMove).encode()
            connectionSocket.send(sendData)
            board.playMoveOnBoard(2,board.lastMove)
            lblTurn["text"] = "opponent"
            print(sendData)    
            play()

def clicked4():
    global finish,board
    if start and user and btn4["text"]==" ":   #For getting the text of a button
        if board.lastMove == player1:
            btn4["text"]="X"
            board.lastMove = username
            sendData = '{}-{}'.format("3",board.lastMove).encode()
            connectionSocket.send(sendData)
            board.playMoveOnBoard(3,board.lastMove)
            lblTurn["text"] = "opponent"
            print(sendData)    
            play()

def clicked5():
    global finish,board
    if start and user and btn5["text"]==" ":   #For getting the text of a button
        if board.lastMove == player1:
            btn5["text"]="X"
            board.lastMove = username
            sendData = '{}-{}'.format("4",board.lastMove).encode()
            connectionSocket.send(sendData)
            board.playMoveOnBoard(4,board.lastMove)
            lblTurn["text"] = "opponent"
            print(sendData)     
            play()

def clicked6():
    global finish,board
    if start and user and btn6["text"]==" ":   #For getting the text of a button
        if board.lastMove == player1:
            btn6["text"]="X"
            board.lastMove = username
            sendData = '{}-{}'.format("5",board.lastMove).encode()
            connectionSocket.send(sendData)
            board.playMoveOnBoard(5,board.lastMove)
            lblTurn["text"] = "opponent"
            print(sendData)   
            play()

def clicked7():
    global finish,board
    if start and user and btn7["text"]==" ":   #For getting the text of a button
        if board.lastMove == player1:
            btn7["text"]="X"
            board.lastMove = username
            sendData = '{}-{}'.format("6",board.lastMove).encode()
            connectionSocket.send(sendData)
            board.playMoveOnBoard(6,board.lastMove)
            lblTurn["text"] = "opponent"
            print(sendData)  
            play()

def clicked8():
    global finish,board
    if start and user and btn8["text"]==" ":   #For getting the text of a button
        if board.lastMove == player1:
            btn8["text"]="X"
            board.lastMove = username
            sendData = '{}-{}'.format("7",board.lastMove).encode()
            connectionSocket.send(sendData)
            board.playMoveOnBoard(7,board.lastMove)
            lblTurn["text"] = "opponent"
            print(sendData)    
            play()

def clicked9():
    global finish,board
    if start and user and btn9["text"]==" ":   #For getting the text of a button
        if board.lastMove == player1:
            btn9["text"]="X"
            board.lastMove = username
            sendData = '{}-{}'.format("8",board.lastMove).encode()
            connectionSocket.send(sendData)
            board.playMoveOnBoard(8,board.lastMove)
            lblTurn["text"] = "opponent"
            print(sendData)    
            play()


def play():
    global isCon,start,user,close
    finish,won = board.isGameFinished()
    if finish:
        answer = messagebox.askyesno("Question","Do you want to play again?")
        if answer:
            sendData = '{}'.format("Play Again").encode()
            connectionSocket.send(sendData)
            board.recordGamePlayed()
            reset()
        else:
            isCon = False
            sendData = '{}'.format("Fun Times").encode()
            connectionSocket.send(sendData)
            connectionSocket.close()
            start = False
            user = False
            close = True
            comData = board.computeStats()
            lblGames["text"] = comData["numGames"]
            lblWon["text"] = comData["wins"]["X"]
            lblLost["text"] = comData["loss"]["X"]
            lblTies["text"] = comData["ties"]
            lblTurn["text"] = "You"
            reset()
            

def reset():
    board.resetGameBoard()
    board.lastMove = player1
    btn1["text"]=" "
    btn2["text"]=" "
    btn3["text"]=" "
    btn4["text"]=" "
    btn5["text"]=" "
    btn6["text"]=" "
    btn7["text"]=" "
    btn8["text"]=" "
    btn9["text"]=" "
    

def updateBoard():
    if int(pos) == 0:
        btn1["text"]="O"
    elif int(pos) == 1:
        btn2["text"]="O"
    elif int(pos) == 2:
        btn3["text"]="O"
    elif int(pos) == 3:
        btn4["text"]="O"
    elif int(pos) == 4:
        btn5["text"]="O"
    elif int(pos) == 5:
        btn6["text"]="O"
    elif int(pos) == 6:
        btn7["text"]="O"
    elif int(pos) == 7:
        btn8["text"]="O"
    elif int(pos) == 8:
        btn9["text"]="O"

btn1 = Button(leftFrame, text=" ",bg="yellow", fg="Black",width=8,height=3,font=('Times', 26),command=clicked1)
btn1.grid(column=1, row=1, sticky = S+N+E+W)
btn2 = Button(leftFrame, text=" ",bg="yellow", fg="Black",width=8,height=3,font=('Times', 26), command=clicked2)
btn2.grid(column=2, row=1, sticky = S+N+E+W)
btn3 = Button(leftFrame, text=" ",bg="yellow", fg="Black",width=8,height=3,font=('Times', 26),command=clicked3)
btn3.grid(column=3, row=1, sticky = S+N+E+W)
btn4 = Button(leftFrame, text=" ",bg="yellow", fg="Black",width=8,height=3,font=('Times', 26),command=clicked4)
btn4.grid(column=1, row=2, sticky = S+N+E+W)
btn5 = Button(leftFrame, text=" ",bg="yellow", fg="Black",width=8,height=3,font=('Times', 26),command=clicked5)
btn5.grid(column=2, row=2, sticky = S+N+E+W)
btn6 = Button(leftFrame, text=" ",bg="yellow", fg="Black",width=8,height=3,font=('Times', 26),command=clicked6)
btn6.grid(column=3, row=2, sticky = S+N+E+W)
btn7 = Button(leftFrame, text=" ",bg="yellow", fg="Black",width=8,height=3,font=('Times', 26),command=clicked7)
btn7.grid(column=1, row=3, sticky = S+N+E+W)
btn8 = Button(leftFrame, text=" ",bg="yellow", fg="Black",width=8,height=3,font=('Times', 26),command=clicked8)
btn8.grid(column=2, row=3, sticky = S+N+E+W)
btn9 = Button(leftFrame, text=" ",bg="yellow", fg="Black",width=8,height=3,font=('Times', 26),command=clicked9)
btn9.grid(column=3, row=3, sticky = S+N+E+W)

btnConnect=Button(rightFrame3, text="Connect", font=('arial', 17, 'bold'), height = 1, width =20,command=clickConnect)
btnConnect.grid (row=2, column=0 ,padx=6, pady=11)

btnQuit=Button (rightFrame3, text="Quit", font=('arial', 17, 'bold'), height = 1, width =20, command = clickQuit) 
btnQuit.grid(row=3, column=0 ,padx=6, pady=10)

lbl=Label(rightFrame2, font=('arial', 20, 'bold'), text="Games:",padx=2, pady=2, bg="Cadet Blue") 
lbl.grid (row=0, column=0, sticky=W)
lblGames=Label(rightFrame2, font=('arial', 20, 'bold'), text=" ",padx=2, pady=2, bg="Cadet Blue",width=10) 
lblGames.grid (row=0, column=1, sticky=W)
lbl=Label(rightFrame2, font=('arial', 20, 'bold'), text="Won:",padx=2, pady=2, bg="Cadet Blue") 
lbl.grid (row=1, column=0, sticky=W)
lblWon=Label(rightFrame2, font=('arial', 20, 'bold'), text=" ",padx=2, pady=2, bg="Cadet Blue",width=10) 
lblWon.grid (row=1, column=1, sticky=W)
lbl=Label(rightFrame2, font=('arial', 20, 'bold'), text="Lost:",padx=2, pady=2, bg="Cadet Blue") 
lbl.grid (row=2, column=0, sticky=W)
lblLost=Label(rightFrame2, font=('arial', 20, 'bold'), text=" ",padx=2, pady=2, bg="Cadet Blue",width=10) 
lblLost.grid (row=2, column=1, sticky=W)
lbl=Label(rightFrame2, font=('arial', 20, 'bold'), text="Ties:",padx=2, pady=2, bg="Cadet Blue") 
lbl.grid (row=3, column=0, sticky=W)
lblTies=Label(rightFrame2, font=('arial', 20, 'bold'), text=" ",padx=2, pady=2, bg="Cadet Blue",width=10) 
lblTies.grid (row=3, column=1, sticky=W)

lbl=Label(rightFrame1, font=('arial', 20, 'bold'), text="Player2:",padx=2, pady=2, bg="Cadet Blue") 
lbl.grid (row=0, column=0, sticky=W)
lblUsername=Label(rightFrame1, font=('arial', 20, 'bold'), text="",padx=2, pady=2, bg="Cadet Blue",width=10) 
lblUsername.grid (row=0, column=1, sticky=W)
lbl=Label(rightFrame1, font=('arial', 20, 'bold'), text="Turn: ",padx=2, pady=2, bg="Cadet Blue") 
lbl.grid (row=1, column=0, sticky=W)
lblTurn=Label(rightFrame1, font=('arial', 20, 'bold'), text="You",padx=2, pady=2, bg="Cadet Blue",width=10) 
lblTurn.grid (row=1, column=1, sticky=W)


window.mainloop()

class Board:

    def __init__(self,user2):
        self.board = [0,0,0,0,0,0,0,0,0]
        self.user1 = "player1"
        self.user2 = user2
        self.lastMove = ""
        self.numGames = 1
        self.wins = {"X": 0, "O": 0}
        self.loss = {"X": 0, "O": 0}
        self.ties = 0


    def recordGamePlayed(self):
        self.numGames = self.numGames + 1

    def resetGameBoard(self):
        self.board = [0,0,0,0,0,0,0,0,0]

    def playMoveOnBoard(self,position,player):
        if player == "player1":
            self.board[position] = "O"
            self.lastMove = "player1"
        else:
            self.board[position] = "X"
            self.lastMove = self.user2

    def isBoardFull(self):
        for cell in self.board:
            if cell == 0:
                return False
        
        return True

    def isGameFinished(self):

        finish = False
        won = None
        b1 = self.board[0]
        b2 = self.board[1]
        b3 = self.board[2]
        b4 = self.board[3]
        b5 = self.board[4]
        b6 = self.board[5]
        b7 = self.board[6]
        b8 = self.board[7]
        b9 = self.board[8]

        if (b1==b2 and b1==b3 and b1=="O") or (b4==b5 and b4==b6 and b4=="O") or (b7==b8 and b7==b9 and b7=="O"):
            finish = True
            won = "O"
            self.wins["O"] = self.wins["O"] + 1
            self.loss["X"] = self.loss["X"] + 1
        elif (b1==b2 and b1==b3 and b1=="X") or (b4==b5 and b4==b6 and b4=="X") or (b7==b8 and b7==b9 and b7=="X"):
            finish = True
            won = "X"
            self.wins["X"] = self.wins["X"] + 1
            self.loss["O"] = self.loss["O"] + 1
        elif (b1==b4 and b1==b7 and b1=="O") or (b2==b5 and b2==b8 and b2=="O") or (b3==b6 and b3==b9 and b3=="O"):
            finish = True
            won = "O"
            self.wins["O"] = self.wins["O"] + 1
            self.loss["X"] = self.loss["X"] + 1
        elif (b1==b4 and b1==b7 and b1=="X") or (b2==b5 and b2==b8 and b2=="X") or (b3==b6 and b3==b9 and b3=="X"):
            finish = True
            won = "X"
            self.wins["X"] = self.wins["X"] + 1
            self.loss["O"] = self.loss["O"] + 1
        elif (b1==b5 and b1==b9 and b1=="O") or (b7==b5 and b7==b3 and b7=="O"):
            finish = True
            won = "O"
            self.wins["O"] = self.wins["O"] + 1
            self.loss["X"] = self.loss["X"] + 1
        elif (b1==b5 and b1==b9 and b1=="X") or (b7==b5 and b7==b3 and b7=="X"):
            finish = True
            won = "X"
            self.wins["X"] = self.wins["X"] + 1
            self.loss["O"] = self.loss["O"] + 1
        elif self.isBoardFull():
            finish = True
            self.ties = self.ties + 1

        return finish,won


    def computeStats(self):
        stats = {}
        stats["board"] = self.board
        stats["user1"] = self.user1
        stats["user2"] = self.user2
        stats["lastMove"] = self.lastMove
        stats["numGames"] = self.numGames
        stats["wins"] = self.wins
        stats["loss"] = self.loss
        stats["ties"] = self.ties

        return stats

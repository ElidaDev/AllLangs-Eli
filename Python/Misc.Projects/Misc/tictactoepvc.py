import string
import random as rand

gameBoard = [
["1", "2", "3"],
["4", "5", "6"],
["7", "8", "9"]   
]

selection = {
    1:[0,0],
    2:[0,1],
    3:[0,2],
    4:[1,0],
    5:[1,1],
    6:[1,2],
    7:[2,0],
    8:[2,1],
    9:[2,2]
}

#print the board
def drawBoard(board):
    for r in range(3):
        print(f"{board[r][0]}|{board[r][1]}|{board[r][2]}")
        print(f"-"*5)
    pass

def checkDraw(board):
    for eachRow in board:
        if any(char in string.digits for char in eachRow):
            return False
    print("Tie")
    return True

def checkHorizontal(board):
        for r in range(len(board)):    
            if board[r][0] != any(char in string.digits for char in board[r][0]):
                if(board[r][0]==board[r][1] and board[r][0] == board[r][2]):
                    symbol = board[r][0]
                    print(f"Winner: {symbol}")
                    return True
            else:
                return False

def checkVertical(board):
        for c in range(len(board)):    
            if board[0][c] != any(char in string.digits for char in board[0][c]):
                if(board[0][c]==board[1][c] and board[0][c] == board[2][c]):
                    symbol = board[0][c]
                    print(f"Winner: {symbol}")
                    return True
            else:
                return False
                
def checkDiagonal(board):
        if board[0][0] != any(char in string.digits for char in board[0][0]):
            if (board[0][0] == board[1][1] and board[0][0] == board[2][2]):
                symbol = board[0][0]
                print(f"Winner: {symbol}")
                return True
            elif (board[0][2] == board[1][1] and board[0][0] == board[2][0]):
                symbol = board[0][2]
                print(f"Winner: {symbol}")
                return True
        else:
            return False
        
def checkWinner(board):
    drawBoard(board)
    if not checkDraw(board):
        if checkHorizontal(board):
            return True
        elif checkVertical(board):
            return True
        elif checkDiagonal(board):
            return True
        else:
            return False
    else:
        return True

def swapTurn(turn):
    if turn:
        return 'X'
    else:
        return 'O'

def checkSpot(symbol,board,row,col):
    if board[row][col] != 'X' and board[row][col] != 'O':
        board[row][col] = symbol
        return False
    return True

symbol = 'X'
turn = True
print("Welcome to TicTac Toe")

while(symbol != 'q'):
    if symbol == 'X':    
        print("")
        drawBoard(gameBoard)
        valid = False

        while not valid:
            print("")
            spot = int(input("Select a spot: "))-1
            print("")
            if spot in range(9):
                row = selection[spot+1][0]
                col = selection[spot+1][1]
                if checkSpot(symbol,gameBoard,row,col):
                    print("Spot Taken")
                else:
                    valid = True
                    
        if checkWinner(gameBoard): 
            symbol = 'q'

        if symbol != 'q':
            symbol = 'O'
    else:
        valid = False
        while not valid:
            spot = rand.randint(1,9)
            row = selection[spot][0]
            col = selection[spot][1]
            if checkSpot(symbol,gameBoard,row,col):
                print("Spot Taken")
            else:
                valid = True

        symbol = 'X'
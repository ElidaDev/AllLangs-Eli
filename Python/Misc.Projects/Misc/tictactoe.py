sampleBoard = [
["1", "2", "3"],
["4", "5", "6"],
["7", "8", "9"]    
]

gameBoard = [
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]    
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

def draw(board):
    for eachRow in board:
        if not (" " in eachRow):
            print("Tie")
            return False

def checkWinner(board):
    if not draw(board):
        for r in range(len(board)):    
            if board[r][0] != " ":
                if(board[r][0]==board[r][1] and board[r][0] == board[r][2]):
                    print(f"Win")
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
    drawBoard(sampleBoard)
    print("")
    drawBoard(gameBoard)
    valid = False

    while not valid:
        spot = int(input("Select a spot: "))-1
        if spot in range(9):
            row = selection[spot+1][0]
            col = selection[spot+1][1]
            if checkSpot(symbol,gameBoard,row,col):
                print("Spot Taken")
            else:
                valid = True
                
    if checkWinner(gameBoard): 
        symbol = 'q'

    if symbol == 'X':
        symbol = "O"
    elif symbol == 'O':
        symbol = 'X'
    else:
        symbol = 'q'
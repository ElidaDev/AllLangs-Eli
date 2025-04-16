import pandas
        
def importWords():
    words = ["Hexadecimal","Bander"]
    #words = ["Binary","Computer","Hexadecimal","Bander","Powershell","Apps","Duck","VSC","Poptarts"]#Input("")
    return words

def importBoard():
    board = pandas.read_csv("wordPractice.csv",header=None)
    rows,cols = board.shape
    return board,rows,cols
print(importBoard())


def printBoard(board):
     pass


def searchHorizontally(board,word,rows,cols):
    # Forward
    for r in range(rows):
        for c in range(cols):
            print(c[0])
            for i in range(len(word)):
                if board[r][c + i] != word[i]:
                    match = False
                    break
            if match:
                return (r, c)  # Return the starting position of the word
    return None  # Word not found
    # Backward

def searchVerically(word,board):
     return

def searchRightDiagonal(word,board):
     return

def searchLeftDiagonal(word,board):
     return
'''
Binary (vert normal)
Computer (diagonal downToRight)
Hexadecimal (horizontal backwards)
Bander (horizontal normal)
Powershell (diagonal upToLeft)
Apps (vertical backwards)
Web Sites (Boggle)
Duck (diagonal downToLeft)
VSC (diagonal upToRight)
Poptarts (vertical normal)
'''
wordSearchBoard=importBoard()
board, rows, cols = importBoard()
words = importWords()

print(f'''
      
Original Board
{printBoard(wordSearchBoard)}

''')

#TODO:  Between these two print statements, you will run all of your searches.

for word in words:
    word = word.upper()
    search = searchHorizontally(board, word, rows, cols)
    if search:
        print(f"Found '{word}' at row {search[0]}, from column {search[1]} to {(search[1])+len(word)}")
    else:
        print(f"'{word}' not found horizontally")
    

print(f'''
      
Answer Board
{printBoard(wordSearchBoard)}

''')
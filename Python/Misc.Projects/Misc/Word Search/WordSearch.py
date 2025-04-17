import pandas
        
def importWords():
    words = ["Binary","Computer","Hexadecimal","Bander","Powershell","Apps","Duck","VSC","Poptarts"]
    return words

def importBoard():
    board = pandas.read_csv("wordPractice.csv",header=None)
    rows,cols = board.shape
    return board,rows,cols

#All of the searches use the same basic principles
'''
for each row or column
    for each row or column
        For each LETTER in the word:
            if the letter is right continue
            else break and try next row col pair
'''
def searchHorizontally(board,word,rows,cols):
    for r in range(rows):
        # Forward search
        for c in range(cols - len(word) + 1): 
            for i in range(len(word)):
                match = True
                if str(board.iloc[r, c + i]).lower() != word[i].lower(): # checks for word forwards
                    match = False
                    break
            if match:
                return (r, c,False)
        for c in range(len(word)-1,cols): 
            for i in range(len(word)):
                match = True
                if str(board.iloc[r, c - i]).lower() != word[i].lower(): # checks for word backwards
                    match = False
                    break
            if match:
                return (r, c-len(word)+1,True)
    return None

def searchVerically(board,word,rows,cols):
    for c in range(cols):
        # Forward search
        for r in range(rows - len(word) + 1): 
            for i in range(len(word)):
                match = True
                if str(board.iloc[r+i, c]).upper() != word[i].upper(): # checks for word forwards
                    match = False
                    break
            if match:
                return (r, c,False)
        for r in range(len(word)-1,rows): 
            for i in range(len(word)):
                match = True
                if str(board.iloc[r-i, c]).upper() != word[i].upper(): # checks for word backwards
                    match = False
                    break
            if match:
                return (r, c-len(word)+1,True)
    return None
    
def searchDiagonallyRight(board,word,rows,cols):
    for r in range(rows):
        # Forward search
        for c in range(cols - len(word) + 1): 
            if (r + len(word) <= rows) and (c + len(word) <= cols):
                for i in range(len(word)):
                    match = True
                    # Down right
                
                    if str(board.iloc[r+i, c+i]).upper() != word[i].upper(): # checks for word forwards
                        match = False
                        break
                    if match:
                        return (r, c, False)
                    #up right
                for i in range(len(word) -1):
                    match = True
                    if str(board.iloc[r-i, c+i]).upper() != word[i].upper(): # checks for word backwards
                        match = False
                        break
                    if match:
                        return (r, c, True)
    return None

def searchDiagonallyLeft(board, word, rows, cols):
    for r in range(rows):
        for c in range(cols):
            #  Down left
            if r + len(word) <= rows and c - len(word) + 1 >= 0:
                match = True
                for i in range(len(word)):
                    if str(board.iloc[r + i, c - i]).upper() != word[i].upper():
                        match = False
                        break
                if match:
                    return (r, c, False)

            # Up left 
            if r - len(word) + 1 >= 0 and c - len(word) + 1 >= 0:
                match = True
                for i in range(len(word)):
                    if str(board.iloc[r - i, c - i]).upper() != word[i].upper():
                        match = False
                        break
                if match:
                    return (r - len(word) + 1, c - len(word) + 1, True)

    return None

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
{board}

''')

for word in words:
    word = word.upper()
    search = searchHorizontally(board, word, rows, cols)
    if search:
        flip = search[2]
        if flip:
            print(f"Found '{word}' at row {search[0]+1}, from column {(search[1])+len(word)+1} to {search[1]+1} ")
        else:    
            print(f"Found '{word}' at row {search[0]+1}, from column {search[1]+1} to {(search[1])+len(word)+1}")
    else:
        search = searchVerically(board, word, rows, cols)
        if search:
            flip = search[2]
            if flip:
                print(f"Found '{word}' from row {search[0]+1} {(search[0])+len(word)+1}, at column {search[1]+1} ")
            else:    
                print(f"Found '{word}' from row {search[0]+1} to {(search[0])+len(word)+1}, at column {search[1]+1}")
        else:
            search = searchDiagonallyRight(board, word, rows, cols)
            if search:
                flip = search[2]
                if flip:
                    print(f"Found '{word}' from row {search[0]+1} {(search[0])+len(word)+1}, from column {(search[1])+len(word)+1} to {search[1]+1}")
                else:    
                    print(f"Found '{word}' from row {search[0]+1} to {(search[0])+len(word)+1},from column {search[1]+1} to {(search[1])+len(word)+1}")
            else:
                search = searchDiagonallyLeft(board, word, rows, cols)
                if search:
                    flip = search[2]
                    if flip:
                        print(f"Found '{word}' from row {search[0]+1} {(search[0])+len(word)+1}, from column {(search[1])+len(word)+1} to {search[1]+1}")
                    else:    
                        print(f"Found '{word}' from row {search[0]+1} to {(search[0])+len(word)+1},from column {search[1]+1} to {(search[1])+len(word)+1}")
                else:
                    print(search)
                

print(f'''
      
Answer Board


''')
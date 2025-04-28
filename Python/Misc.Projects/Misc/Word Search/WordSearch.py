import pandas
        
def importWords():
    words = ["Powershell","Apps","Duck","VSC","Poptarts","WebsiTes"] #"Binary","Computer","Hexadecimal","Bander"
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
        for r in range(rows - len(word),cols): 
            for i in range(len(word)):
                match = True
                if str(board.iloc[r-i, c]).upper() != word[i].upper(): # checks for word backwards
                    match = False
                    break
            if match:
                return (r, c,True)
    return None
    
def searchDiagonally(board, word, rows, cols):
    for r in range(rows):
        for c in range(cols):
            # \ top-left to bottom-right
            if r + len(word) <= rows and c + len(word) <= cols:
                match = True
                for i in range(len(word)):
                    if str(board.iloc[r + i, c + i]).upper() != word[i].upper():
                        match = False
                        break
                if match:
                    return (r, c, False,True)

            # \ bottom-right to top-left Checked 
            if r - len(word) >= -1 and c - len(word) >= -1:
                match = True
                for i in range(len(word)):
                    if str(board.iloc[r - i, c - i]).upper() != word[i].upper():
                        match = False
                        break
                if match:
                    return (r, c, False, None)

            # / Up-Right (bottom-left to top-right) Checked
            if r - len(word) >= -1 and c + len(word) <= cols:
                match = True
                for i in range(len(word)):
                    if str(board.iloc[r - i, c + i]).upper() != word[i].upper():
                        match = False
                        break
                if match:
                    return (r, c, True, None)

            # / Down-Left (top-right to bottom-left)
            if r + len(word) <= rows and c - len(word) >= -1:
                match = True
                for i in range(len(word)):
                    if str(board.iloc[r + i, c - i]).upper() != word[i].upper():
                        match = False
                        break
                if match:
                    return (r, c, False,False)

    return None


def Boggle(board, word, rows, cols):#
    directions = [ 
        (0, 1),    # right
        (0, -1),   # left
        (1, 0),    # down
        (-1, 0),   # up
        (1, 1),    # down-right
        (-1, -1),  # up-left
        (-1, 1),   # up-right
        (1, -1)    # down-left
    ]
    visited = []

    #Make a board of False
    for i in range(rows):
        visited.append([False] * cols)

    for r in range(rows):
        for c in range(cols):
            if str(board.iloc[r, c]).upper() == word[0]:#Find first letter
                points = []
                match = True
                points.append([r, c]) #Add first letter is in points
                visited[r][c] = True 
                for i in range(1, len(word)): #Start at the second letter, because we know the first one is good
                    foundNext = False
                    for dx, dy in directions:
                        nr = r + dx
                        nc = c + dy
                        if nr >= 0 and nr < rows and nc >= 0 and nc < cols and not visited[nr][nc]: #Make sure it is within the rows and cols and it has not been visited already
                            if str(board.iloc[nr, nc]).upper() == word[i]: #Check each letter
                                points.append([nr, nc]) #Append the points if the letter is right
                                #print(word[i]) #For debugging :)
                                visited[nr][nc] = True #Set each letter that matches to true
                                r, c = nr, nc  # Update the next letter's position
                                foundNext = True 
                                break
                    if not foundNext:  # If no valid position was found, we try again
                        match = False
                        break
                if match:
                    return (r, c, points)

                #Reset visited grid for next search
                for i in range(rows):
                    for j in range(cols):
                        visited[i][j] = False

    return None # This hurt my brain i dont like boggle :cry face:




'''
Binary (vert normal) Good
Computer (diagonal downToRight)
Hexadecimal (horizontal backwards) Good
Bander (horizontal normal) Good 
Powershell (diagonal upToLeft)
Apps (vertical backwards) Good
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
    print()
    search = searchHorizontally(board, word, rows, cols)
    if search:
        print(f"Found {word} Horizontally.")
        flip = search[2]
        if flip:
            print(f"1Found '{word}' at row {search[0]+1}, from column {(search[1])+len(word)} to {search[1]}")

        else:    
            print(f"2Found '{word}' at row {search[0]+1}, from column {search[1]+1} to {(search[1])+len(word)}")
    else:
        search = Boggle(board,word,rows,cols)
        if search:
             print(search[2])

        # search = searchVerically(board, word, rows, cols)
        # if search:
        #     print(f"Found {word} Vertically.")
        #     flip = search[2]
        #     if flip:
        #         print(f"Found '{word}' from row {search[0]} to {(search[0])-len(word)-1}, at column {search[1]+1} ")
        #     else:    
        #         print(f"Found '{word}' from row {search[0]} to {(search[0])+len(word)+1}, at column {search[1]+1}")
        # else:
        #     search = searchDiagonally(board, word, rows, cols)
        #     if search:
        #         print(f"Found {word} Diagonally.")
        #         flip = search[2]
        #         if flip: # Works for Top right to bottom left
        #             print(f"1Found '{word}' from row {search[0]+len(word)} to {(search[0])+1}, from column {(search[1])+1} to {search[1]-len(word)+2}")
        #         else:   # Works for Bottom right to top left \
        #             if search[3] == None:
        #                 print(f"2Found '{word}' from row {search[0]+1} to {(search[0])+len(word)+1},from column {search[1]+1} to {(search[1])-len(word)+1}")
        #             if search[3]:
        #                 print(f"3Found '{word}' from row {search[0]+1} to {(search[0])+len(word)+1},from column {search[1]+1} to {(search[1])-len(word)+1}")
        #             if search[3] == False:
        #                 print(f"4Found '{word}' from row {search[0]+1} to {(search[0])+len(word)+1},from column {search[1]+1} to {(search[1])-len(word)+1}")
                
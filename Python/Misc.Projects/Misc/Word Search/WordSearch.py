import pandas
        
def importWords():
    words =[
    "Android", "Androidstudio", "Application", "Applicationprograminterface", "Array",
    "Artificialinteligence", "Ascii", "Authentication", "Autonomous", "Backend",
    "Bandwidth", "Bash", "Beier", "Bigdata", "Binary", "Bios", "Bit", "Bladerunner",
    "Block", "Blockbase", "Blockbasecoding", "Blockly", "Bluepillattack", "Body",
    "Boolean", "Booleanexpression", "Bootstrap", "Boyles", "Brandle", "Bruteforce",
    "Bug", "Byte", "Calloway", "Camelcase", "Cascadingstylesheets", "Cd",
    "Centralprocessingunit", "Character", "Chickenjockey", "Chipset", "Class",
    "Client", "Code", "Coffee", "Commandline", "Comments", "Complier", "Computation",
    "Computer", "Concatenation", "Conditionalstatement", "Constraint", "Container",
    "Cook", "Copyright", "Cpucooler", "Crontab", "Csharp", "Csv", "Cybersecurity",
    "Data", "Database", "Datastructure", "Datatype", "Debugging", "Decryption",
    "Deeplearning", "Directory", "Disksorage", "Div", "Document",
    "Documentobjectmodel", "Domainnamesystem", "Doom", "Drycode", "Edit", "Edwards",
    "Efficiency", "Email", "Encapsulation", "Encryption", "Entitycomponentsystem",
    "Environmentvariable", "Epkins", "Ethernet", "Eventhandler", "Eventlistener",
    "Executable", "Exploit", "Extensiblemarkuplanguage", "Fileexplorer", "Firefly",
    "Firewall", "Firmware", "Fisher", "Flask", "Float", "Footer", "Framework",
    "Frontend", "Function", "Garbagecollection", "Ghostinshell", "Gigabyte",
    "Github", "Globalvariable", "Godelnumbering", "Google", "Graphicaluserinterface",
    "Graphicscard", "Greenwald", "Grumpycat", "Halflife", "Harddrive", "Hardware",
    "Hashing", "Header", "Heatsink", "Hexadecimal", "Hitchhiker", "Hollywood",
    "Hoodie", "Hooper", "Hypertextmarkuplanguage", "Hypertexttransferprotocol", "If",
    "Ifstatement", "Img", "Import", "Index", "Infiniteloop", "Inheritance",
    "Inlaystyle", "Input", "Integer", "Integrateddevelopmentenvironment", "Internet",
    "Internetofthings", "Internetprotocol", "Interpreter", "Intrusiondetection",
    "Java", "Javascript", "Jpg", "KAPLEWSKI", "KERNEL", "KEYBOARD", "KEYESCROW",
    "KISNER", "KLEPTOGRAPHY", "KOTLIN", "KUBERNETES", "LAPTOP", "LATENCY", "LEAF",
    "LIBRARY", "LINK", "LINUX", "LIST", "LOCALAREANETWORK", "LOCALVARIABLE", "LOGIC",
    "LONG", "LOOP", "MACADDRESS", "MACHINELEARNING", "MACOS", "MAIN", "MALWARE",
    "MARIADATABASE", "MARKUP", "MARTZ", "MATPLOTLIB", "MATRIX", "MCCORMICK",
    "MEDIAACCESSCONTROLADDRESS", "MEMORY", "METHOD", "MINECRAFT", "MITAPPINVENTOR",
    "MONITOR", "MOUSE", "NANO", "NETSTAT", "NETWORK", "NEURALNETWORK", "NMAP",
    "NODE", "NOSQL", "NOTEPAD", "NYANCAT", "OBJECT", "OCTOCAT",
    "OPENSYSTEMSINTERCONNECTIONMODEL", "OPERATINGSYTEM", "OSBORNEPIKE", "OUTPUT",
    "PACKET", "PACMAN", "PANDAS", "PASSWORD", "PAYNE", "PENETRATIONTESTING", "PEPE",
    "PERIPHERAL", "PHISHING", "PHONE", "PHP", "PIPES", "PIZZA", "POINTER",
    "POLYMORPHISM", "PONG", "PORTAL", "POWERSHELL", "POWERSUPPLY", "PRINTER",
    "PROCESS", "PROGRAMMING", "PROJECTOR", "PROPERTY", "PROTOCOL", "PSEUDOCODE",
    "QUERY", "RANDOMACCESSMEMORY", "RANSOMWARE", "RASPBERRYPI", "RECURSION",
    "REPLIT", "ROUTER", "RUBBERDUCK", "RUBY", "RUSSELL", "RUST", "SCRIPT", "SCRUM",
    "SDK", "SECURITY", "SECURITYBASELINE", "SERVER", "SHELL", "SILICONVALLEY",
    "SLACK", "SMITH", "SOCKET", "SOFTWARE", "SOLIDSTATEDRIVE", "SPOOFING", "SPRITES",
    "SQL", "SSH", "STARTREK", "STARWARS", "STEVEJOBS", "STORYPOINT", "STRING",
    "STRUCTUREDQUERYLANGUAGE", "STYLING", "SWIFT", "SWITCH", "TABLET", "TAGS",
    "TCP", "TERMINAL", "TESTING", "TEXTUSERINTERFACE", "THREAD", "TRANSACTION",
    "TRANSFORM", "TRANSMISSIONCONTROLPROTOCOL", "TURTLE", "TUX", "VARIABLE", "VIM",
    "VIRTUALIZATION", "VIRTUALPRIVATENETWORK", "VIRUS", "VISUALSTUDIOCODE",
    "VULNERABILITY", "WEBPAGE", "WEBSITE", "WHILE", "WIDEAREANETWORK", "WIFI",
    "WIKIPEDIA", "WINDOWS", "WINDOWSPOWERSHELL", "WIRESHARK", "WONG", "WORM",
    "ZELDAZERODAY", "ZOOKOSTRIANGLE"
]

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
    return None#searchVerically

def searchVerically(board, word, rows, cols):
    for c in range(cols):  # Loop over each column
        # Forward search (top to bottom)
        for r in range(rows - len(word) + 1):
            match = True
            for i in range(len(word)):
                if str(board.iloc[r + i, c]).upper() != word[i].upper():
                    match = False
                    break
            if match:
                return (r, c, False)  # False = not backwards

        # Backward search (bottom to top)
        for r in range(len(word) - 1, rows):
            match = True
            for i in range(len(word)):
                if str(board.iloc[r - i, c]).upper() != word[i].upper():
                    match = False
                    break
            if match:
                return (r, c, True)  # True = backwards
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
    search = searchHorizontally(board, word, rows, cols)
    if search:
        print(f"Found {word} Horizontally.")
        flip = search[2]
        if flip:
            print(f"1Found '{word}' at row {search[0]+1}, from column {(search[1])+len(word)} to {search[1]}")

        else:    
            print(f"2Found '{word}' at row {search[0]+1}, from column {search[1]+1} to {(search[1])+len(word)}")
    else:
        #search = Boggle(board,word,rows,cols)
        #if search:
        #     print(word)
        #     print(search[2])

        search = searchVerically(board, word, rows, cols)
        if search:
            print(f"Found {word} Vertically.")
            flip = search[2]
            if flip:
                print(f"Found '{word}' from row {search[0]} to {(search[0])-len(word)-1}, at column {search[1]+1} ")
            else:    
                print(f"Found '{word}' from row {search[0]} to {(search[0])+len(word)+1}, at column {search[1]+1}")
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
                
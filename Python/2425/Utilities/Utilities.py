from fractions import Fraction
##### Text modification #####

#Text color

def colorize(color,message):
    '''
    Available colors:
        Black,
        Blue,
        Cyan,
        Green,
        Magenta,
        Red,
        Yellow,
        And more to come
    '''
    color = color.lower()
    if color == "red":
        return (f"\033[31m{message}\033[39m")
    elif color == "black":
        return (f"\033[30m{message}\033[39m")
    elif color == "green":
        return (f"\033[32m{message}\033[39m") 
    elif color == "yellow":
        return (f"\033[33m{message}\033[39m") 
    elif color == "blue":
        return (f"\033[34m{message}\033[39m") 
    elif color == "magenta":
        return (f"\033[35m{message}\033[39m") 
    elif color == "cyan":
        return (f"\033[36m{message}\033[39m") 
    elif color == "white":
        return (f"\033[37m{message}\033[39m")
    elif color == "bold":
        return (f"\033[37m{message}\033[0m")

##### List checking ######

# bool if check in list

def checkWord (check, validlist):
    '''
    Checks if the given word(check) is in the given list.
    '''
    validlist = [x.lower() for x in (validlist)]
    check = check.lower()
    return check in validlist

# word if check in list  
  
def userInput(question,correctAnswers):
    '''
    Only allows the user input to be one of the answers in the list (noncase sensitive).
    '''
    ui=input(question)
    while(not(ui.lower() in correctAnswers)):
        ui=input(question)
    ui = ui.title()
    return ui

# Check for float

def checkUserInput(message,z):
    ui = ""
    while ui.upper() !='Q':
        ui = input(message)
        if ui.upper() != 'Q':
            z.append(float(ui))

## List cleaning

def noDupeList (list):
    '''
    Removes duplicates from a list
    '''
    for x in list:
        if list.count(x) > 1:
            del list[list.index(x)]
    return list

def remCharList (list,char):
    '''
    removes given characters from all items in list.
    '''
    for i in range(len(list)):
        list[i] = list[i].replace(char,"")
    return list
    
###### File IO ##### 

#Get Data

def getData(fileName):
    '''
    Gets data from a file.
    '''
    data = []
    with open(fileName, "r") as file:
        for line in file:
            data.append(line.rstrip())
    return data

#Check if file contains an item

def checkFile(fileName, item):
    '''
    Checks if a piece of data is in a file.
    '''
    inFile = False
    with open(fileName, "r") as file:
        for line in file:
            if item in line:
                inFile = True
    return inFile
    
#Check how many times an item occurs

def countOccurences(fileName, item, column):
    '''
    Counts how many times an item occurs in a file.
    
    FileName is the name of the file to check
    item is the item to count in the file
    column is the column the data is in, 0 if there are no commas seperating it from the start.
    '''
    itemCount = 0
    with open(fileName, "r") as file:
        for line in file:
            data = line.rstrip().split(", ")
            if data[column] == item:
                itemCount += 1
    return itemCount

###### Math ######

#Divide two lists and return results

def divideTwoLists(top,bottom):
    '''
    Divides two lists and return results
    '''
    results = []
    readableResults = []
    for i in range(len(bottom)):
        for j in range(len(top)):
            # Calculate the division
            divisionResult = Fraction(top[j], bottom[i])
            results.append(float(divisionResult))
            readableResults.append(str(divisionResult))
    return results,readableResults

# Factors Readable

def factors(number):
    '''
    Returns the factors of the given number
    Format: list[num*num2,num3*num4...]
    '''
    multiples = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            multiples.append(f"{number//i}*{i}")
    return multiples

# Factors Useable

def factorsTypeTwo(number):
    '''
    Returns the factors of a given number
    Format: list[num,num2...]
    '''
    multiples = []
    for i in range(1,number+1):
        if number/i == round(number/i):
            multiples.append(int(number/i))
            multiples.append(int(i))
    return noDupeList(multiples)

#Quadratic formula

def quadratic(a,b,c):   
    '''
    Returns quadratic formula.
    ''' 
    a,b,c = int(a),int(b),int(c)    
    return(f"({b*-1} + sqrt({(b*b)-(4*a*c)})) / {2*a}"),(f"({b*-1} - sqrt({(b*b)-(4*a*c)})) / {2*a}")

#Equation for two perfect cubes    

def cubeeq(a,b,sign):    
    '''
    Returns equation from perfect cubes
    '''
    if sign == "+":    
        return(f'''
        ({a}+{b})(({a}^2)-({a}*{b})+({b}^2))
        ''')
    else:
        return(f'''
        ({a}-{b})(({a}^2)+({a}*{b})+({b}^2))
        ''')

# Synthetic division math 
       
def syntheticdiv(x,lc,p):
    '''
    Finds 0's and does synthetic divison
    x should = "N" if no known zeros.
    '''
    zeros = []
    remainder = -256
    answers = []
    # Do the math
    answers.append(lc[0])
    if x != 'N':
        for i in range(1, len(lc)):
            answers.append(lc[i]+(answers[i-1]*(x)))
        #Get remainder out of answers
        remainder = answers.pop()
        #Make output easier to read
        for i in range(len(answers)-1):
            exponent = len(answers) - i - 1
            answers[i] = f"{answers[i]}(x)^{exponent}"
        return answers,f'Remainder: {remainder}',f'x={x}'
    
    else:   
        a = 0
        b = True
        while b:
            try:    
                x = p[a]
            except IndexError:
                print(f"All values checked!")
                break
            for i in range(1, len(lc)):
                answers.append(lc[i]+(answers[i-1]*(x)))
            #Get remainder out of answers
            remainderpos = answers.pop()
            if remainderpos != 0:  
                answers = [] 
                answers.append(lc[0])
                for j in range(1, len(lc)):
                    answers.append(lc[j]+(answers[j-1]*(x*-1)))
                remainderneg = answers.pop()
                if remainderneg != 0:
                    #Print remainder if it is close to 0
                    if (remainderneg > -1 and remainderneg < 1) or (remainderpos > -1 and remainderpos < 1):     
                        print(f"{p[a-1]:.2f} FAILED, +r = {remainderpos:.2f}, -r = {remainderneg:.2f}")  
                    remainderneg = None
                    remainderpos = None
                else:
                    remainderneg = None
                    zeros.append(x*-1)
            else: 
                remainderpos = None
                zeros.append(x)
            a += 1
        return f'zeroes={zeros}'


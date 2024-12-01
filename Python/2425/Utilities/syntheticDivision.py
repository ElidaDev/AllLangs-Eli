equation = []
posibilitiesp = []
posibilitiesq = []
posibilities = []
known = input("If x is known enter it, otherwise enter a non numeric value: ")

def checkUserInput(message,z):
    ui = ""
    while ui.upper() !='Q':
        ui = input(message)
        if ui.upper() != 'Q':
            z.append(float(ui))

def syntheticdiv(x,lc):
    print(posibilities)
    p = list(posibilities)
    # X = y if known N if a 
        # Define Variables*
    remainder = -256
    answers = []
    # Do the math
    answers.append(lc[0])
    if x != 'N':
        for i in range(1, len(lc)):
            answers.append(lc[i]+(answers[i-1]*(x)))
        #Get remainder out of answers
        remainder = answers.pop()
        #Make it easier to read
        for i in range(len(answers)-1):
            exponent = len(answers) - i - 1
            answers[i] = f"{answers[i]}(x)^{exponent}"
    else:
        a = 0
        b = True
        while b:
            try:    
                x = p[a]
            except IndexError:
                print("Value Failed all checks, you forgot a possibility or it is no solution.")
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
                    a +=1
                    print(f"{p[a-1]} FAILED, +r = {remainderpos}, -r = {remainderneg}")  
                    remainderneg = None
                    remainderpos = None
                else:
                    x = x *-1
                    b = False
            else: 
                b = False


       #Make it easier to read
    for i in range(len(answers)-1):
        exponent = len(answers) - i - 1
        answers[i] = f"{answers[i]}x^{exponent}"
    return answers,f'Remainder: {remainder}',f'x={x}'

# Set known to N if value is unknown
try:
    float(known)
except ValueError:
    known = "N"

checkUserInput("Next Value in order for equation ('Q' to stop): ", equation)
checkUserInput("Next Value in order for possibilites (A) ('Q' to stop): ", posibilitiesp)
checkUserInput("Next Value in order for possibilites (C) ('Q' to stop): ", posibilitiesq)
# Reset ui 

for i in range(len(posibilitiesq)):
    for j in range(len(posibilitiesp)):    
        posibilities.append(float(posibilitiesp[j]/posibilitiesq[i]))

print(posibilities)

print(syntheticdiv(known,equation))

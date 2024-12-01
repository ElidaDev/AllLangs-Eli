from fractions import Fraction

def noDupeList (list):
    for x in list:
        if list.count(x) > 1:
            del list[list.index(x)]
    return list

def checkUserInput(message,z):
    ui = ""
    while ui.upper() !='Q':
        ui = input(message)
        if ui.upper() != 'Q':
            z.append(float(ui))

def factors(number):
    multiples = []
    for i in range(1,number+1):
        if number/i == round(number/i):
            multiples.append(int(number/i))
            multiples.append(int(i))
    return noDupeList(multiples)

def syntheticdiv(x,lc,m=None):
    zeros = []
    p = posibilities
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
       #Make it easier to read
# Variables
equation = []
posibilitiesp = []
posibilitiesq = []
posibilities = []
posibilitiesprint = []
known = input("If x is known enter it, otherwise enter a non numeric value: ")
#Setup Equation
checkUserInput("Next Value in order for equation ('Q' to stop): ", equation)
posibilitiesp = factors(int(equation[-1]))
posibilitiesq = factors(int(equation[0]))
# Set known to N if value is unknown
try:
    float(known)
except ValueError:
    known = "N"


for i in range(len(posibilitiesq)):
    for j in range(len(posibilitiesp)):
        # Calculate the division
        division_result = Fraction(posibilitiesp[j], posibilitiesq[i])
        posibilities.append(float(division_result))
        posibilitiesprint.append(str(division_result))
print(f'''

{posibilitiesp}      
____________________________      
{posibilitiesq}

Possibilites:''')
for fraction , decimal in noDupeList(list(zip(posibilitiesprint, posibilities))):
    print(f'\t{decimal} - > {fraction} ')
print()
print(syntheticdiv(known,equation))

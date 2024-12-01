equation = []
posibilities = []
known = input("If x is known enter it, otherwise enter a non numeric value: ")


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
            print(p)
            print(p[a])
            x = p[a]
            print(x)
            for i in range(1, len(lc)):
                answers.append(lc[i]+(answers[i-1]*(x)))
            #Get remainder out of answers
            remainder = answers.pop()
            if remainder != 0:  
                answers = [] 
                answers.append(lc[0])
                for j in range(1, len(lc)):
                    answers.append(lc[j]+(answers[j-1]*(x*-1)))
                remainder = answers.pop()
                if remainder != 0:
                    a +=1
                    print(f"{p[a-1]} FAILED")
                    x = p[a]  
                else:
                    x = x *-1
                    b = False
            else: 
                x = p[a]
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
# Reset ui to a random string value
ui = '.'
#Get equation nums
while ui.upper() != 'Q':
    ui = input("Next Value in order for equation ('Q' to stop): ")
    if ui.upper() != "Q":    
        equation.append(float(ui))
# Reset ui to a random string value
ui = '.'
#Get Possible positive x values
if known == "N":
    while ui.upper() != 'Q':
        ui = input("Next Value for possibilities ('Q' to stop): ")
        if ui.upper() != "Q":    
            posibilities.append(float(ui))


print(syntheticdiv(known,equation))

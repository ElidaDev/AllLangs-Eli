# bool if check in list
def checkWord (validlist, check):
    validlist = [x.lower() for x in (validlist)]
    check = check.lower()
    return check in validlist

# List cleaning
def noDupeList (list):
    for x in list:
        if list.count(x) > 1:
            del list[list.index(x)]
    return list

def noSpaceList (list):
    for i in range(len(list)):
        list[i] = list[i].replace(" ","")
    return list
#Math 
def factors(number):
    multiples = []
    for i in range(1,number+1):
        if number/i == round(number/i):
            multiples.append(f"{int(number/i)}*{i}")
    return multiples

def quadratic(a,b,c):    
    a,b,c = int(a),int(b),int(c)    
    return(f"({b*-1} + sqrt({(b*b)-(4*a*c)})) / {2*a}"),(f"({b*-1} - sqrt({(b*b)-(4*a*c)})) / {2*a}")
    
def cubeeq(a,b,sign):    
    if sign == "+":    
        return(f'''
        ({a}+{b})(({a}^2)-({a}*{b})+({b}^2))
        ''')
    else:
        return(f'''
        ({a}-{b})(({a}^2)+({a}*{b})+({b}^2))
        ''')
        
def syntheticdiv(x,lc):
    # Define Variables
    answers = []
    # Do the math
    if x != 'N':
        answers.append(lc[0])
        for i in range(1, len(lc)):
            answers.append(lc[i]+(answers[i-1]*x))
        #Get remainder out of answers
        remainder = answers.pop()
        #Make it easier to read
        for i in range(len(answers)-1):
            exponent = len(answers) - i - 1
            answers[i] = f"{answers[i]}x^{exponent}"

    return answers,f'Remainder: {remainder}'
#Untested below

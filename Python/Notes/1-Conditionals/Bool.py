'''
    Boolean Expressions and Operators

    boolean - True or False
    operator - math functions +,-,*,/

    logic operators - 
        <       less than
        >       greater than
        <=      less than or equal to
        >=      greater than or equal to
        ==      is it equal to
        !=      is it not equal to
        not     pythonic ! or opposite of the boolean exp to the right
        and &&  both exp on both sides of the and is true
        or ||   only one exp on either side of the or is true
    
    Boolean expression is any combination of boolean values and logic operators. 
 
'''

print(4 < 6) #True
print()
print(4<7 and 3 > 1) #True
x=4

print()
print(x != 5) #True
print()
print(True == False) #False
print()
print(True != False) #True
print()
print(True and False) #False
print()
print(True and True) #True

# Conditionals read left to right

print()
print(True and False or True)
print()
print(bool("False")) #True
print()
print(bool("True")) #True
print()
print(bool("")) #False

# IF it is not 0 then it is true
# 


guesses = 5
secretNumber = 7    
while True:
    while True:
        try:
            x = int(input("Number: "))
            break
        except ValueError:
            print("Please insert an integer")
    if guesses >= 1:
        guesses -= 1
        if x > secretNumber:
            print("The number you guessed is bigger than the correct number!")
        elif x < secretNumber:
            print("The number you guessed is less than the correct number!")
        else:
            print("You got the number!")
    else:
        print("You ran out of guesses!")
        break


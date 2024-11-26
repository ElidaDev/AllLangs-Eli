import random
import string
ui = "Input 'q' to quit"
while ui != 'q':
    print("Input 'q' to quit or Enter to continue")
    ui = input()
    # Password requirements
    numLower = int(input("Enter the number of lowercase letters: "))
    numUpper = int(input("Enter the number of uppercase letters: "))
    numDigits = int(input("Enter the number of numbers: "))
    numSpecial = int(input("Enter the number of special characters: "))

    #Simplifing string.#### 
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()"
    password = []


    for i in range(numLower):
        password.append(random.choice(lowercase))
    for i in range(numUpper):
        password.append(random.choice(uppercase))
    for i in range(numDigits):
        password.append(random.choice(digits))
    for i in range(numSpecial):
        password.append(random.choice(special))

    # Shuffle shuffles the list
    random.shuffle(password)

    # concatinate
    pword = ''.join(password)

    print("Generated Password:", pword)

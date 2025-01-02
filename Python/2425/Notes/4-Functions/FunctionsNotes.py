#### Functions ####

#Add some numbers

def addTwo(a,b):
    print(a+b)
    
addTwo(1,53)

print()

#Testing try except stuff :)
loop = True
while loop:
    try:
        ui = input("Enter a number: ")
        if int(ui) == round(int(ui)):
            print("Check pass")
            loop = False
        else:
            raise ValueError("Please enter an integer!")
    except ValueError as errorMessage:
        x = errorMessage
        print(x)
        if "base" in x:
            print("Hi")
#        if "base 10" in errorMessage:
#            errorMessage = "Please enter an integer!"
#        print(f"Check failed {errorMessage}")
#Conditionals = If something is true, then something happens
'''
    Conditionals is usually the if then statements

    if something is true:
        do this
    
    if boolean expression is true:
        do this
'''

masterUsername = "admin"
masterPassword = "123456"

username = input("username: ")
password = input("password: ")

if username == masterUsername:
    print("username is correct")

'''
    else statements - trigger when everything else fails
'''

if username == masterUsername:
    print("username is correct")
else:
    print("username is not correct")

'''
    So far you only have 2 options
        basically a yes or no question

    Multiple options or else if
        else if -> elif
'''

if username == masterUsername:
    print("username is correct")
elif username == masterPassword:
    print("username and password should not be the same")
else:
    print("username is not correct")

'''
    Nested conditional Statements
        Nested = code that is indented under another line of code

    if this is true:
        if this is true:
            then do this

    error:  indentation is incorrect or indentation error
        check your tabs and indentation for each line of code
'''

if username == masterUsername:
    print("username is correct")
    if password == masterPassword:
        print("Welcome to the program")
    else:
        print("credentials are not correct")
else:
    print("credentials are not correct")

'''
    Complex Conditional Statements
        and -> checks if the boolean exp on both sides of the and statement equal true
        or  -> checks if the boolean exp on both sides of the or is at least one true
'''
if username == masterUsername and password == masterPassword:
    print("welcome to the program")
else:
    print("credentials are not correct")









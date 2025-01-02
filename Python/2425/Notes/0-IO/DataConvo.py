'''
    Data Types
        Primitive
            - boolean = 1 or 0 = True or False
                Smallest data type you could ever have
            - integers = whole number (+/-)
            - float = decimal number
            - Char = a single ASCII value

        Non-Primitive
            - Sequence Data
                - String - Sequence of chars concatenated
                - List 
                - Tuple
                - Dicts/HashMap/JSON
            - Objects and Classes

'''



email = "example@example.com"

print(len(email))

#Binary of a letter
#ord() converts ascii to int 
#bin() converts int to bin
#chr() int to ascii

print(bin(ord("l")))
index = email.find('@')
username = email[0:index]
print(username)
print(email[0:5])

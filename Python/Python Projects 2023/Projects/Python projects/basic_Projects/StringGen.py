import random
import string

Special = ["!", "@", "#", "$", "%", "^", "&", "*"]
capital = input("Capital letters(y/n): ")
numbers = input("Numbers (y/n): ")
special = input("Special characters (y/n): ")
N = int(input("Length of string: "))

characterSet = string.ascii_letters

if capital == "y":
    characterSet += string.ascii_uppercase
if numbers == "y":
    characterSet += string.digits
if special == "y":
    characterSet += string.punctuation

print(''.join(random.choices(characterSet, k=N)))
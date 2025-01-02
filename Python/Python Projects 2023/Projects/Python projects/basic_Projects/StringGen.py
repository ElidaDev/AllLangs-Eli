import random
import string

Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Special = ["!", "@", "#", "$", "%", "^", "&", "*"]
Lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Capital = random.choice(Lowercase).capitalize

Cap = input("Capital letters(y/n)> ")
Num = input("Numbers (y/n)> ")
Special = input("Special characters (y/n)> ")
N = int(input("Length of string> "))
Strng = []

if Cap == "y" and Num == "y" and Special == "n": 
    print(''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=N)))
if Cap == "y" and Num == "n" and Special == "n": 
    print(''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=N)))
if Cap == "n" and Num == "y" and Special == "n": 
    print(''.join(random.choices(string.ascii_lowercase + string.digits, k=N)))
if Cap == "y" and Num == "y" and Special == "y": 
    print(''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + Special, k=N)))
if Cap == "y" and Num == "n" and Special == "y": 
    print(''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase  + Special, k=N)))
if Cap == "n" and Num == "y" and Special == "y": 
    print(''.join(random.choices(string.ascii_lowercase + string.digits + Special, k=N)))
if Cap == "n" and Num == "n" and Special == "n": 
    print(''.join(random.choices(string.ascii_lowercase, k=N)))
if Cap == "n" and Num == "n" and Special == "y": 
    print(''.join(random.choices(string.ascii_lowercase + Special, k=N)))
import random
import sys
x = 0
rangemax = 10
rangemin = 1

guesses = 0
secretNumber = random.randint(rangemin,rangemax)
    

while x != secretNumber:
    x = (rangemin+rangemax)//2
    if x > rangemin:
        x -= 1
    guesses += 1
    if x > secretNumber:
        print(f"{x} is bigger than the correct number!")
        rangemax = x-1
    elif x < secretNumber:
        print(f"{x} is less than the correct number!")
        rangemin = x+1
    else:
        print(f"CPU got the number ({x}) in {guesses} guesses!")

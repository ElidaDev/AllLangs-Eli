import random as rdm
import time

Sides = int(input("How many sides on the dice: "))
Dice = int(input("How many dice: "))
Waittime = int(input("Wait between dice rolls: "))
Rolls = []

for i in range(Dice):
    time.sleep(Waittime)
    x = rdm.randint(1, Sides)
    Rolls.append(x)
print(Rolls)
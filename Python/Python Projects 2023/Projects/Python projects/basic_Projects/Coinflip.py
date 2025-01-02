import random as rdm

Tosses = int(input("How many tosses: "))
Flips = []

for i in range(Tosses):
    x = rdm.randint(1, 2)
    if x == 1:
        Flips.append("Heads")
    if x == 2:
        Flips.append("Tails")
print(Flips)


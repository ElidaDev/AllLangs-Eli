import random as rdm

Tosses = int(input("How many tosses: "))
Flips = []

for i in range(Tosses):
    x = rdm.randint(1, 2)
    if x == 1:
        Flips.append("Heads")
    else:
        Flips.append("Tails")
print(Flips)


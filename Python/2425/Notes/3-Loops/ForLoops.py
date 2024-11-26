### For loops ##

#for i in range(10):
#    print(i)
#
#for i in range(10,20):
#    print(i)
#    
#for i in range(0,20,2):
#    print(i)
#    
#for i in range(20,1,-2):
#    print(i)
import random

name = "yyyyyy aeiou"
vowelCount = 0
chance = random.randint(0,1)
for i in range(len(name)):
    if chance == 1:    
        if name[i].lower() in "aeiouy":
            vowelCount += 1
    else:
        if name[i].lower() in "aeiou":
            vowelCount += 1
print(vowelCount)
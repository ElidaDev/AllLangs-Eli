#Print out 0-max
#max = 96
#i=0
#
#while(i <= max):
#    print(i)
#    i+=1
#
#ui = ""
#    
#while(ui!="What?"):
#    ui = input("Guess what? ")
#print("Never mind...")
#

import string

# print 9-0
i = 9
while(i >= 0):
    print(i)
    i-=1
print()   
i = 0

#print evens up to 20
while(i <= 20):
    if not(i % 2):
        print(i)
    i += 1
print()
i = 0  

#print odds up to 20  
while(i <= 20):
    if i % 2:
        print(i)
    i += 1
print()   
i = 0

#print 0-50 every 5
while(i <= 50):
    print(i)
    i += 5
print()
i = 65

#print ascii_uppercase using chr

while(i<=90):
    print(chr(i))
    i+=1
print()
i=0

#print ascii_uppercase using string lib

while(i<len(string.ascii_uppercase)):
    print(string.ascii_uppercase[i])
    i+=1
print()    
i = -10

#print in range -10,11

while(i in range(-10, 11)):
    if not(i % 2):
        print(i)
    i += 1
print()

print(string.ascii_uppercase)


import random as rand
fileName = "Classroom.txt"
students=["Mike","Riley","Eli","Ezra","Deggvin","Scott","Johana","Wesley", "Nolan"]
studentid=["15","23","33","5","6","3","7","35","9"]
studentcolor=["Green","Chartreuse","Cyan","Red","Blue","Pink","Yellow","Grey","Blue"]
# Create #
def createFile(fileName,Data):
    with open(fileName,"w+") as file:
        out = ""
        for i in Data:
            out+=i+"\n"
        file.write(out)
        file.close()
        
def writeFile(fileName,Data):
    with open(fileName,"w") as file:
        out = ""
        for i in Data:
            out+=i+"\n"
        file.write(out)
        file.close()

def readFile(fileName):
    with open(fileName,"r") as file:

        EntireFile = file.readlines()
        file.close()
    return EntireFile

def appendFile(fileName,Data):
    with open(fileName,"a") as file:
        file.write(Data)
        file.close()

# for i in range(len(students)):
#     r = rand.randint(2,4)*(rand.randint(1,10)*.1)
#     with open(f"Students/{students[i]}.txt", "w+") as file:
#         Data = f'''
#         Student Id: {studentid[i]}
#         Gpa: {r:.2f}
#         Favorite Color: {studentcolor[i]}
#         '''
#         file.write(f"{students[i]}'s Profile{Data}\n")    
# file.close()

# Write #

# with open(fileName, "w") as file:
#     students=["Mike","Riley","Eli","Ezra","Deggvin","Scott","Johana","Wesley", "Nolan"]
#     studentid=["15","23","33","5","6","3","7","35","9"]
#     out=""
#     for i in range(len(studentid)):
#         out+=f"{bin(int(studentid[i])).strip("0b").zfill(8)}, {students[i]}\n" # The id is returned as a string, Converted to an Int --> Binary --> removes 0b --> makes sure it is a byte long

#     file.write(out)
#     file.close()

# Read #

# with open(fileName,"r") as file:

#     EntireFile = file.readlines()
    
#     print("".join(EntireFile))
#     file.close()

# Append #

# with open(fileName,"a") as file:
#     newStudent = "00000000, Bander\n"

#     file.write(newStudent)
#     file.close()

# Update #
# with open(fileName,"r") as file:

#     EntireFile = file.readlines()
#     file.close()


cleanData = []
for eachLine in EntireFile:
    cleanData.append(eachLine.rstrip())
print(cleanData)
for i in range(len(studentcolor)):
    cleanData[i]+=f", {studentcolor[i]}\n"
print(cleanData)

with open(fileName,"w") as file:
    out=""
    for i in range(len(cleanData)):
        out+=cleanData[i]
    file.write(out)
    file.close()
# Delete #

# with open(fileName,"r") as file:
#     EntireFile = file.readlines()
#     file.close()

def removeData(fileName,Data):
    EntireFile = readFile(fileName)

    for i in range(len(EntireFile)-1):
        if Data in EntireFile[i]:
            EntireFile.pop(i)

    with open(fileName,"w") as file:
        out=""
        for i in range(len(EntireFile)):
            out+=EntireFile[i]
        file.write(out)
        file.close()
idtoremove = "00000111"



with open("Classroom.txt","w") as file:
    #data to write 
    out=""
    for i in range(len(EntireFile)):
        out+=EntireFile[i]
    
    #writing the data
    file.write(out)
    file.close()  #If you do not close 

print(EntireFile)


fileName = "Classroom.txt"
students=["Mike","Riley","Eli","Ezra","Deggvin","Scott","Johana","Wesley", "Nolan"]
studentid=["15","23","33","5","6","3","7","35","9"]
# Create #

with open(fileName,"w+") as file:

    students=["Mike","Riley","Eli","Ezra","Deggvin","Scott","Johana","Wesley", "Nolan"]
    out = ""
    for eachName in students:
        out+=eachName+"\n"
    file.write(out)
    
    file.close

for i in range(len(students)):
    with open(f"Students\{students[i]}.txt", "w+") as file:
        Data = f'''
        Student Id: {studentid[i]}
        '''
        file.write(f"{students[i]}'s Profile{Data}\n")    

# Write #
with open(fileName, "w") as file:
    students=["Mike","Riley","Eli","Ezra","Deggvin","Scott","Johana","Wesley", "Nolan"]
    studentid=["15","23","33","5","6","3","7","35","9"]
    out=""
    for i in range(len(studentid)):
        out+=f"{bin(int(studentid[i])).strip("0b").zfill(8)}, {students[i]}\n" # The id is returned as a string, Converted to an Int --> Binary --> removes 0b --> makes sure it is a byte long

    file.write(out)
    file.close()
# Read #
with open(fileName,"r") as file:

    EntireFile = file.readlines()
    
    print("".join(EntireFile))
    file.close()
# Append #
with open(fileName,"a") as file:
    newStudent = "0, Bander\n"
    file.write(newStudent)


    file.close()
# Update #

# Delete #




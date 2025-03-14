import pandas as pd
import matplotlib.pyplot as plt
FDF = pd.read_csv("Data/Foyer.csv",header=0)
PDF = pd.read_csv("Data/Programs.csv",header=0)

schools = FDF["school"].unique()

programs = PDF["program"].unique()

# Found via library
merged = FDF.merge(PDF, on="id", how="inner", )

# print(merged[["firstName","lastName","program"]])
StudsByPrograms = merged.groupby("program")["school"].apply(list)
print(StudsByPrograms)
count = []
attendence = []
school = []
pgram = []
for eachSchool in schools:
    for eachProgram in StudsByPrograms.items():
        program = eachProgram[0]
        schoolList = list(eachProgram[1])
        pgram.append(program)
        attendence.append(schoolList.count(eachSchool))
        school.append(eachSchool)
        count.append(f"{program}: {eachSchool}({schoolList.count(eachSchool)})\n")

print(attendence)
print(pgram)
print(list(zip(pgram,school,attendence)))

#I learned the lamda function on my own during first semester some time, and it's just being used to show what to sort the list by here. sorting by program, and attendence in the program in reverse order
# Zip just combines lists Which i also learned sometime before this class.
i=0
for p, s, a in sorted(list(zip(pgram,school,attendence)), key=lambda x: (x[0],-x[2]),reverse=False):
    i += 1
    print(f"Program: {p}, School: {s}, Attendance: {a}")
    if not(i % 23):
        print()
print(len(schools))




# import matplotlib.pyplot as plt
# import numpy as np

# # Sample Data (Make sure pgram, school, and attendance are lists of equal length)
# data = list(zip(pgram, school, attendence))

# # Get unique programs and schools
# uniquePrograms = sorted(set(pgram))  
# uniqueSchools = sorted(set(school))  

# # Create a dictionary Chat gpt assisted
# attendanceDict = {program: {s: 0 for s in uniqueSchools} for program in uniquePrograms}

# for prog, sch, att in data:
#     attendanceDict[prog][sch] += att  


# xLabels = uniquePrograms  
# x = np.arange(len(xLabels)) 

# # Prepare bars for each school
# fig, ax = plt.subplots(figsize=(12, 6))  # Set figure size

# # Plot bars for each school #Chat gpt assisted with "Enumerate"
# for i, sch in enumerate(uniqueSchools):
#     yValues = [attendanceDict[prog][sch] for prog in xLabels]  # Get attendance per program
#     ax.bar(x + i * .2, yValues, width=.2, label=sch) 

# # Formatting the plot
# ax.set_xlabel("Programs")
# ax.set_ylabel("Attendance Count")
# ax.set_title("School Attendance Across Programs")
# ax.set_xticks(x + .2 / 2)  # Center x-axis labels
# ax.set_xticklabels(xLabels, rotation=45, ha="right")  # Rotate labels for readability
# ax.legend(title="Schools")  # Add legend for schools

# plt.show()  # Display the plot


# pcount = PDF.value_counts("program")
# print(pcount)

# pcount.plot(kind="bar", color="green", edgecolor="black")
# plt.xlabel("Programs")
# plt.ylabel("Students")
# plt.xticks(rotation=45, ha="right") 
# plt.title("# of students per program")
# plt.show()

# scount = FDF.value_counts("school")
# print(scount)

# scount.plot(kind="bar", color="green", edgecolor="black")
# plt.xlabel("Schools")
# plt.ylabel("Students")
# plt.xticks(rotation=45, ha="right") 
# plt.title("# of students per school")
# plt.show()

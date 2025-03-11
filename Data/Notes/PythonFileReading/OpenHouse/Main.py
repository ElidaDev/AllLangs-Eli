import pandas as pd
import matplotlib.pyplot as plt
FDF = pd.read_csv("Data/Foyer.csv",header=0)
PDF = pd.read_csv("Data/Programs.csv",header=0)

schools = FDF["school"].unique()

programs = PDF["program"].unique()

# Found via library
merged = FDF.merge(PDF, on="id", how="inner", )

# print(merged[["firstName","lastName","program"]])
StudsByPrograms = merged.groupby("program")["emailAddress"].apply(list)
print(StudsByPrograms)

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

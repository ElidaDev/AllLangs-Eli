import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Data/EstoreData.csv")

#1   , 2, 3   , 4   , 5         , 6              , 7  , 8  , 9        , 10
#time,ip,email,state,phoneNumber,textNotification,card,cost,department,company



#Calculate each department's spending
spendings = []

departments = list(df["department"].unique())

for eachDepartment in departments:
    spending = 0
    for i in range(len(df)):
        if df["department"][i]== eachDepartment:
            spending += float(df["cost"][i])
    spendings.append([spending,eachDepartment])
costs =[]
depts =[]
for i in range(len(spendings)):
    costs.append(spendings[i][0])
    depts.append(spendings[i][1])

# print(costs,"\n",depts)
# plt.bar(depts,costs)
# plt.title("Costs per department")
# plt.ylim(1500000,2500000)
# plt.ylabel("Cost")
# plt.xlabel("Department")
# plt.xticks(rotation=45)
# plt.show()
        
spendings.sort(reverse=True)
d = []
c = []
print(spendings)
print(len(spendings))    
for i in range(22-5,22):
    c.append([spendings[i][0]])
    d.append([spendings[i][1]])
for i in range(6):
    c.append([spendings[i][0]])
    d.append([spendings[i][1]])

print(d,c)
plt.plot(d, c, marker='o', linestyle='-', color='b', label="Total Purchase Amount")
plt.xlabel("Purchase Amount")
plt.ylabel("Category")
plt.legend()
plt.show()
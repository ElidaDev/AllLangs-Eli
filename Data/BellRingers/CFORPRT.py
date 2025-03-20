import pandas as pd
import re
import matplotlib.pyplot as plt
df = pd.read_csv("Data/EstoreData.csv")

#1   , 2, 3   , 4   , 5         , 6              , 7  , 8  , 9        , 10
#time,ip,email,state,phoneNumber,textNotification,card,cost,department,company



#Calculate each department's spending
spendings = []

departments = list(df["department"].unique())
#0, 192, 127, or 255 at the start of the string before the first .
# ^ start of string , (x|y|z) x y or z, \. matches the . at the end of the numbers 
pattern = r"\@"
# Remove rows where 'ip' matches the pattern list comprehension, learned back when we were doing basic lists, it basically means if ip not match pattern keep it in the list, its similar to dictionairy comprehension.
df = df[~df["ip"].str.match(pattern)]

# Calculate spending by department  using . sum adds all the costs per department, and then resets the index back to being in order using .reset_index()
spendingsDf = df.groupby('department')['cost'].sum().reset_index()
# Convert to list
# Found itterrows while looking through the docs
spendings = []
for i, row in spendingsDf.iterrows():
    spendings.append([row['cost'], row['department']])

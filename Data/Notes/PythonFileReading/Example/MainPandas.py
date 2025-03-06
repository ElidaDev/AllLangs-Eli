import pandas as pd

fn = "first_name"
sc = "integer"


#read the data (df)
df = pd.read_csv("highscores.csv",header=0)
names=df[fn]
scores=df[sc]

# print(df)
# print(df[fn])
# print(df[sc])

# for eachName in df[fn]:
#     print(eachName)

# for eachScore in df[sc]:
#     print(eachScore)

#Basic Stats

print(f'''
    Max: {scores.max()}
    Min: {scores.min()}
    Range: {scores.max()-scores.min()}
    Mean: {scores.mean()}
    Median: {scores.median()}
    Mode: {scores.mode()}
    STD: {scores.std()}
    Total: {scores.sum()}
      ''')


# Find the scores that are 1000, put the first names in the list of "Highscore"

# Highscore=df.loc[df[sc]==1000,fn]
#iloc is index location
# HighscoreTheFirst=df.loc[df[sc]==1000,fn].iloc[-1]

# print(Highscore)
# by header to sort by, ascending (bool), ignore_index=True/False (if true index is in order if false, index is in original values)
sortedDF= df.sort_values(by='integer',ascending=False)

sortedDF.to_csv("highscores-sorted.csv", index=False)
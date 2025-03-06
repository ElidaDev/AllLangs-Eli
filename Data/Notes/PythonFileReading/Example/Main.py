import Utilities as Utils

entireFile = Utils.readFile("highscores.csv")

clean = []
names = []
scores = []
for eachLine in entireFile:
    name,score = eachLine.split(",")
    name.replace("\n","")
    score.replace("\n","")
    try:
        scores.append(int(score))
        names.append(name)
    except ValueError:
        print(f"Bad Data: {eachLine}")
    clean.append(f"{name}\t{score}")


maxIndex = scores.index(max(scores))
minIndex = scores.index(min(scores))


print(f"1. {names[minIndex]}: {scores[minIndex]}")



Utils.createFile("highscoresclean.txt", clean)
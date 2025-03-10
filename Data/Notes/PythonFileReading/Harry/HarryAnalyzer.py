import glob
import matplotlib.pyplot as plt
import numpy as np
 
books = glob.glob("OriginalData/*.txt")
bookshelf=[]
for eachBook in books:
    name=eachBook[eachBook.index("B"):eachBook.index(".")]
    bookshelf.append(name)
print(bookshelf)
reducing=[]
percents=[]
mentions=[]
for i in range(len(bookshelf)):
    with open(f"OriginalData/{bookshelf[i]}.txt","r", encoding="utf8") as file:
        currentBook=file.readlines()
        file.close
    out=[]
    for eachLine in currentBook:
        if not eachLine == "\n":
            out.append(eachLine)
    #print(len(currentBook))
    #print(len(out))
    percent = float(f"{((1-len(out)/len(currentBook))*100):.1f}")
    percents.append(percent)
    reducing.append(f"{bookshelf[i]} reduced by: {percent}%")
    cleanBook = open(f"CleanData/{bookshelf[i]}.txt","w+", encoding="utf8")
    mentioned =0
    for eachLine in out:
        cleanBook.write(eachLine)
        if not "Rowling" in eachLine:
            theWords = eachLine.split(" ")
            for eachWord in theWords:
                if "Harry" in eachWord:
                    mentioned+=1
    cleanBook.close()
    print(mentioned)
    mentions.append(mentioned)
print(reducing)

#plt.bar(range(1,8),percents)
#plt.ylabel("percent of bloat")
#plt.ylim(30,34)
#plt.xlabel("the books")
#plt.title("bloatware in harry potter")
#plt.show()
plt.bar(range(1,8),mentions)
plt.ylabel("mentions")
plt.xlabel("the books")
plt.title("how many times they say harry in harry potter")
plt.show()

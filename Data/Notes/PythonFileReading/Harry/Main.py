import glob # For multifile reading
import matplotlib.pyplot as plt
import random as rand
books = glob.glob("Data/*.txt")
bookshelf=[]
for eachBook in books:
    bookName= eachBook[eachBook.index("Data\\")+5:eachBook.index(".txt")]
    bookshelf.append(bookName) #eachBook.removeprefix("Data\\").removesuffix(".txt")

print(bookshelf)

reductions = []
amountCompressed = []
count =[]
for i in range(len(books)):
    with open(books[i],"r",encoding="utf8") as file:
        f = file.readlines()
        file.close()

    out = []
    ccount = 0
    for eachLine in f:
        if not eachLine == "\n":
            if "Harry" in eachLine:
                ccount+=1
            out.append(eachLine)
    # print(f)

    # print(len(f))
    # print(len(out))
    cleanFile = open(f"CleanData/Clean-{bookshelf[i]}.txt","w+",encoding="utf8")
    for eachLine in out:
        cleanFile.write(eachLine)
    cleanFile.close()
    reductions.append(f"{float((1-len(out)/len(f))*100):.1f}")
    amountCompressed.append((1-len(out)/len(f))*100)
    count.append(ccount)
print(f"Harry mentioned: {sum(count)} times!")
print(reductions)

for i in range(len(reductions)):
    print(f'''{bookshelf[i]} Reduced by: {reductions[i]}%''')

# plt.bar(range(1,8),amountCompressed)
# plt.title("Amount reduced %")
# plt.xlabel("Book")
# plt.ylabel("% Reduced")
# plt.ylim(30,35)
# plt.show()

plt.bar(range(1,8),count)
plt.title("Harry MENTION!")
plt.xlabel("Book")
plt.ylabel("Mention count: ")
plt.ylim(1000,5500)
plt.show()
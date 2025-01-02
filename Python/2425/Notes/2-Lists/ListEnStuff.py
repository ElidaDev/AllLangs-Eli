'''
    Data Types

    Integer
        Whole Numbers
    Bool
        True or False
    Float
        Decimal numbers
    String
        Sequence of chars
    List
        Sequence of data
        
'''

shoppingList = ["Pickles", "Milk", "Tacos", "Egg White", "Windshield Wipers", "Hot Wheels", "25 lb Bag of Rice"]

#Check for l in each string

for x in shoppingList:
    if "l" in x:
        print(x)

#Print list in readable form

print("\n".join(shoppingList))

for x in shoppingList:
    y = (len(shoppingList[shoppingList.index(x)])/(len(shoppingList)/2))*1.07
    print(f"{x}: ${y:.2f}")


print("\n"*50) #VeRyPrOFSinal clear terminal

#Stats of a list
numbers = [2,3,1,5,6,3,5,7,25.42,426.56]

print(f"Amount of things in list: {len(shoppingList)}")
print(f"Total of the numbers: {sum(numbers)}")
print(f"Minimum of the numbers: {min(numbers)}")
print(f"Maximum of the numbers: {max(numbers)}")
print(f"Average of the numbers: {sum(numbers) / len(numbers)}")

print("\n"*50)

#List modification

backpack = []

backpack.append("TextBook")
backpack.append("Notebook")
backpack.append("Chromebook")

nums = 10

for i in range(2):
    for i in range(nums):
        backpack.append(str(i+1))



print("\n".join(backpack))

for x in shoppingList:
    if shoppingList.count(x) > 1:
        del shoppingList[shoppingList.index(x)]

print("\n".join(backpack))


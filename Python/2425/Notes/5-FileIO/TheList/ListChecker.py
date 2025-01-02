col1 = []
col2 = []
with open("numbers.csv", "r") as file:
    for line in file:
        col1.append(line.rstrip().split(",")[0])
        col2.append(line.rstrip().split(",")[1])
        
def count(col1, col2):
    count = []
    for i in col1:
        counti = 0
        for j in col2:
            if i == j:
                counti += 1
        if counti > 0:        
            count.append(f"{counti},{i}")  
    return count
print(count(col1,col2))    
def countOccurences(fileName, item, column):
    '''
    FileName is the name of the file to check
    item is the item to count in the file
    column is the column the data is in, 0 if there are no commas seperating it from the start.
    '''
    itemCount = 0
    with open(fileName, "r") as file:
        for line in file:
            data = line.rstrip().split(", ")
            if data[column] == item:
                itemCount += 1
    return itemCount

#
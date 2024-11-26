numA = int(input("Please give any number: "))
numB = int(input("Give a number to be added to the first: "))
numAB = numA + numB
print(numAB)
numC = int(input("Give a number to be multiplied by the second number: "))
numBC = numB * numC
print(numBC)
numD = int(input("Give a number to divide the first 3 combined: "))
numDABC = (numA + numB + numC) / numD
print(numDABC)
numE = int(input("Give a number to be subtracted from the previous calculations: "))

numFinal = (numAB + numBC + numDABC) - numE

print(numD/(numA+(numB*numC)-numE)

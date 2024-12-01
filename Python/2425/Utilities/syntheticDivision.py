import utils
from fractions import Fraction
equation = []
posibilities = []
posibilitiesprint = []
known = input("If x is known enter it, otherwise enter a non numeric value: ")
#Setup Equation
utils.checkUserInput("Next Value in order for equation ('Q' to stop): ", equation)
# Set known to N if value is unknown
try:
    float(known)
except ValueError:
    known = "N"
# Print Output
posibilitiesp, posibilitiesq =utils.factorsTypeTwo(int(equation[-1])), utils.factorsTypeTwo(int(equation[0]))
posibilities,posibilitiesprint = utils.divideTwoLists(posibilitiesp,posibilitiesq)
print(f'''\n{posibilitiesp}\n____________________________\n{posibilitiesq}\nPossibilites:''')
#print readable decimal fraction conversion
for fraction , decimal in utils.noDupeList(list(zip(posibilitiesprint, posibilities))):
    print(f'\t{decimal} - > {fraction} ')
print()
print(utils.syntheticdiv(known,equation,posibilities))

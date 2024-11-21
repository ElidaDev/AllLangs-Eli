def checkWord (validlist, check):
    validlist = [x.lower() for x in (validlist)]
    check = check.lower()
    return check in validlist

def noDupeList (list):
    for x in list:
        if list.count(x) > 1:
            del list[list.index(x)]
    return list

def noSpaceList (list):
    for i in range(len(list)):
        list[i] = list[i].replace(" ","")
    return list
    
#Untested below



import Utilities 

def selection(item, prices, pricem, pricel):
    itemDisplay = str(item)
    price = 0
    
    item = Utilities.userInput(f'''
    What size {itemDisplay} do you want? 
        (s) Small = {Utilities.colorize("green",f"${prices:.2f}")}
        (m) Medium = {Utilities.colorize("green",f"${pricem:.2f}")}
        (l) Large = {Utilities.colorize("green",f"${pricel:.2f}")}
        (n) no {itemDisplay}
    ''', ["s","m","l","n"])
    if item == "S":
        item = f"Small {itemDisplay}"
        price = prices
        return price, item
    elif item == "M":
        item = f"Medium {itemDisplay}"
        price = pricem
        return price, item
    elif item == "L":
        item = f"Large {itemDisplay}"
        price = pricel
        return price, item
    else:
        item = ""
        price = 0
        return price, item

    



ui="Welcome to the Krusty Crab"
print(ui)

global completeorder
completeorder = ["Order 0: "]

subtotallist = {}
subtotal = 0
i = 0
while(ui!="checkout"):
#Krabby Patty order
    order=[]
    price, item = selection("Krabby Patty",1.25,2,3)
    subtotal += price
    if len(item) > 1: 
        order.append(f"\t{item}")

#Krabby patty meal    
    price, item = selection("Krabby Patty Meal",1.25,2,3)
    subtotal += price
    if len(item) > 1: 
        order.append(f"\t{item}")

# Wants cheese?
    cheese = Utilities.userInput(f"Would you like to add {Utilities.colorize('green','Sea Cheese')} to that for 25 cents?(y/n): ",["y","n"])
    if cheese == "Y":
        subtotal += .25
        order.append(f"\t + SeaCheese") 

#Coral bits order            
    price, item = selection("CoralBits",1.00,1.25,1.50)
    subtotal += price
    if len(item) > 1: 
        order.append(f"\t{item}")

#Seafoam soda order
    price, item = selection("Seafoam soda",1,1.25,1.50)
    subtotal += price
    if len(item) > 1: 
        order.append(f"\t{item}")
#Kelp Shake Order
    kelpShake = Utilities.userInput(f"Would you like to add a Kelp Shake? ($2.00) (y/n): ",["y","n"])
    if kelpShake == "Y":
        subtotal += 2.00
        order.append(f"\tKelp Shake") 
#Kelp rings order
    kelpRings = Utilities.userInput(f"Would you like to add Kelp Rings? ($1.50) (y/n): ",["y","n"])
    if kelpRings == "Y":
        subtotal += 1.50
        sauce = Utilities.userInput(f"Would you like to add sauce? ($.50) (y/n): ",["y","n"])
        if sauce == "Y":
            subtotal += .5
            order.append(f"\tKelp Rings w/ Sauce") 
        else:
            order.append(f"\tKelp Rings") 
#Salty sea dog  Order
    ssdog = Utilities.userInput(f"Would you like to add a Salty Sea Dog? ($1.25) (y/n): ",["y","n"])
    if ssdog == "Y":
        subtotal += 1.25
        flong = Utilities.userInput(f"Would you like to make it a footlong? (+$.75) (y/n): ",["y","n"])
        if flong == "Y":
            subtotal += .75
            order.append(f"\tFoot Long") 
        else:
            order.append(f"\tSalty Sea Dog")

    #Goldenloaf
    goldenLoaf = Utilities.userInput(f"Would you like to add a golden Loaf? ($2.00) (y/n): ",["y","n"])
    if goldenLoaf == "Y":
        subtotal += 2
        sauce = Utilities.userInput(f"Would you like to add sauce? ($.50) (y/n): ",["y","n"])
        if sauce == "Y":
            subtotal += .5
            order.append(f"\tGolden Loaf w/ Sauce") 
        else:
            order.append(f"\tGolden Loaf") 
    #            
    sailorsSurprise = Utilities.userInput(f"Would you like to add a Sailors Surprise? ($3.00) (y/n): ",["y","n"])
    if sailorsSurprise == "Y":
        subtotal += 3.00
        order.append(f"\tSailor's surprise") 

    nextOrder = Utilities.userInput(f"Would you like to add another order? (y/n): ", ["y","n"])
    subtotallist[i] = (subtotal)
    print(subtotallist)
    #https://stackoverflow.com/questions/6531482/how-to-check-if-a-string-contains-an-element-from-a-list-in-python Someone explained this in the comments
    if (any("Patty" in item for item in order) and any("Seafoam" in item for item in order) and any("CoralBits" in item for item in order)):
        discount = True
        discountAmount = subtotal*.15 
    else:
        discount = False
    completeorder.append("\n".join(order))
    #Set discount
    if discount:
        subtotal -= discountAmount
        completeorder.append(f"{Utilities.colorize('red',f'$-{discountAmount:.2f} discount applied')}")
    if nextOrder == "Y":
        i += 1
        subtotal = f"{subtotal:.2f}"
        completeorder.append(f'Subtotal: {Utilities.colorize("green",f"${subtotal}")}')
        completeorder.append("")
        completeorder.append(f"Order {i}: ")
        subtotal = 0
    else:
        subtotal = f"{subtotal:.2f}"
        completeorder.append(f'Subtotal: {Utilities.colorize("green",f"${subtotal}")}')
        completeorder.append("")
        numberItems = len(order)
        numberOrders = i
        #Modification code
        modify = Utilities.userInput(f"Would you like to modify an order? (y/n)", ["y","n"])
        while modify != "N":
            print("\n".join(completeorder))
            try:
                ordernum = int(input("What order number would you like to modify?"))
                if ordernum > numberOrders or ordernum < 0:
                    print(f"Invalid order number. Please choose a valid order between 0 and {numberOrders}.")
                    continue # retries while loop
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            # Find the index of the selected order number
            minIndex = completeorder.index(f"Order {ordernum}: ") + 1  

            # Find the index of the next order to determine the end of the current order's items
            if (ordernum + 1) <= numberOrders:
                maxIndex = completeorder.index(f"Order {ordernum + 1}: ")  # Next order's starting point
            else:
                maxIndex = len(completeorder)  # Last order, go until the end of the list

            # Show the items for the selected order
            print("Current order items:")
            for item in completeorder[minIndex:maxIndex]:
                print(item)

            # Ask if user wants to delete the order items
            delete_order = input("Do you want to delete this order? (y/n): ")
            if delete_order.lower() == "y":
                del subtotallist[ordernum]
                for i in range(maxIndex - 1, minIndex - 2, -1):  # Reverse iteration to avoid indexing issues
                    del completeorder[i]
                print("Order deleted.")
            
            modify = Utilities.userInput(f"Would you like to modify another order? (y/n)", ["y","n"])
        if input("Would you like to order again? (y/n): ") == "y":
            i = numberOrders+1
            completeorder.append(f"Order {i}: ")
            subtotal = 0
        else:
            ui = "checkout"
# Format, and get full subtotal 
sublist = []       
for x in subtotallist.values():
    sublist.append(x)
subtotal = sum(sublist)
completeorder = "\n".join(completeorder)
#Print reciept
reciept = (f'''
Order total:    
    {completeorder}
Subtotal: {Utilities.colorize("green",f"${subtotal:.2f}")}
Tax:      {Utilities.colorize("green",f"${subtotal*0.07:.2f}")}
Total:    {Utilities.colorize("green",f"${subtotal*1.07:.2f}")}
''')
print(reciept)

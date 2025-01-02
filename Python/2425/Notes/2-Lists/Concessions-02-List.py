#iteration 1:  Order some popcorn
'''
    ask the user for what size popcorn 
        small = $5.00
        med = $6.00
        large = $7.00
    print out their total
        subtotal: $_.__

'''
#Global Variables
subtotal = 0
#order="User's Order\n"
order=[]

popcorn = input('''
What size popcorn do you want? 
    (s) small = $5.00
    (m) medium = $6.00
    (l) large = $7.00
    (n) no popcorn
''')
if popcorn == "s":
    subtotal+=5
    popcorn = "Small"
elif popcorn == "m":
    subtotal+=6
    popcorn = "Medium"
elif popcorn == "l":
    subtotal+=7
    popcorn = "Large"
else:
    subtotal+=0

#order+=f"\t{popcorn} popcorn\n"
order.append(f"{popcorn} popcorn")

print(f"subtotal: ${subtotal}")

#iteration 2:  Order a nice fresh soda pop
'''
    Ask the user for what size soda pop they would want
        small = $3.00
        med = $4.00
        large = $5.00
            ask if they want child size for just $0.38 cents more
    print out their current order and subtotal
        subtotal: $_.__
'''
drink = input('''
What size drink do you want? 
    (s) small = $3.00
    (m) medium = $4.00
    (l) large = $5.00
    (n) no fresh soda pop 
''')
if drink == "s":
    subtotal+=3
    drink = "Small"
elif drink == "m":
    subtotal+=4
    drink = "Medium"
elif drink == "l":
    subtotal+=5
    drink = "Large"
    child = input("Would you like a child size for only $0.38 more? (y/n)")
    if child == "y":
        subtotal+=.38
        drink = "Child"
else:
    subtotal+=0

#order+=f"\t{drink} drink\n"
order.append(f"{drink} drink")

print(order)
print(f"subtotal: ${subtotal}")

#iteration 3 What candy would you like? 
'''
    What type of candy would you like?
        Sour Patch Kids  $2.00
        M & M's          $2.50
            Plain
            Peanuts
            Crunchy
        Licorish         $2.50
            Twizzlers
            Red Vines
    Print the current order
    Print the subtotal
'''

candy = input('''
What kind do you want? 
    (s) Sour Patch Kids = $2.00
    (m) M & M's = $2.50
    (l) Licorish = $2.50
    (n) no candy
''')
if candy == "s":
    subtotal+=2
    candy = "SourPatch"
#elif candy == "m" or "l" or "n":   DO NOT DO THIS!!!
elif candy == "m" or candy == "l":
    subtotal+=2.50
    if candy == "m":
        candyType = input("(Pl}ain or (Pe)anuts or (C)runchy? ")
        candy = f"{candyType} M&M's"
    else:
        candyType = input("(T)wizzlers or (R)ed Vines? ")
        candy = f"{candyType} Licorish" 
else:
    subtotal+=0

#order+=f"\t{candy} candy\n"
order.append(candy)

print(order)
print(f"subtotal: ${subtotal}")

#iteration 4:  Butter toppings do cost... sorry...
'''
    Ask the user for how many pumps of butter they need?
        Each pump = $0.25
    Print out the order
    Print out the subtotal
'''
pumps = int(input("How many pumps ($0.25) of butter would you like? "))
if pumps < 0:
    pumps=0

subtotal += pumps * 0.25
#order+=f"\t{pumps} butter pumps\n"
order.append(pumps)
print(order)
#subtotal:.2f means it will have 2 decimal places
print(f"subtotal: ${subtotal:.2f}")

#iteration 5:  If they ordered popcorn, soda, and candy give them $1.50 off
#                   Checkout with a tax of 7%
'''  Final Output
        User's Order
            popcorn
            drink
            candy
            butter
            y/n for discount

            subtotal
            tax amount
            total
'''
#if not(popcorn=="n" and drink=="n".....
if not("n" in order):
    subtotal -= 1.50
    order.append("Discount: Yes")
    #order+="\ty discount\n"
else:
    order.append("Discount: No")
    #order+="\tn discount\n"

#order+=f"\n\tsubtotal: ${subtotal:.2f}\n"
#order+=f"\ttax:     ${subtotal*.07:.2f}\n"
#order.append(f"subtotal: ${subtotal:.2f}")
#order.append(f"tax: ${subtotal*.07:.2f}")
#subtotal*=1.07
#order+=f"\ttotal:   ${subtotal:.2f}\n"
#order.append(f"total: ${subtotal:.2f}")
#order = "\n".join(order)

receipt =f'''
User's Order:
    {order[0]} 
    {order[1]} 
    {order[2]} 
    {order[3]} pumps of butter
    {order[4]} 
    
    subtotal ${subtotal:.2f}
    tax      ${subtotal*0.07:.2f}
    total    ${subtotal*1.07:.2f}
'''

print(receipt)
###  This version allows for multiple orders 

#iterator var
ui="Welcome to the Tellplace Drive-In South"
print(ui)
completeorder = []
#Global Variables
subtotal = 0
#while boolean expression is true
while(ui!="checkout"):

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
    elif popcorn == "m":
        subtotal+=6
    elif popcorn == "l":
        subtotal+=7
    else:
        subtotal+=0

    #order+=f"\t{popcorn} popcorn\n"
    order.append(popcorn)
    print(order)
    print(f"subtotal: ${subtotal}")


    ############# DRINK SECTION
    drink = input('''
    What size drink do you want? 
        (s) small = $3.00
        (m) medium = $4.00
        (l) large = $5.00
        (n) no fresh soda pop 
    ''')
    if drink == "s":
        subtotal+=3
    elif drink == "m":
        subtotal+=4
    elif drink == "l":
        subtotal+=5
        child = input("Would you like a child size for only $0.38 more? (y/n)")
        if child == "y":
            subtotal+=.38
            drink = "c"
    else:
        subtotal+=0

    #order+=f"\t{drink} drink\n"
    order.append(drink)
    print(order)
    print(f"subtotal: ${subtotal}")


    ################  CANDY SECTION
    candy = input('''
    What type do you want? 
        (s) Sour Patch Kids = $2.00
        (m) M & M's = $2.50
        (l) Licorish = $2.50
        (n) no candy
    ''')
    if candy == "s":
        subtotal+=2
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
    pumps = int(input("How many pumps ($0.25) of butter would you like? "))
    if pumps < 0:
        pumps=0




    #iteration 5
    subtotal += pumps * 0.25
    #order+=f"\t{pumps} butter pumps\n"
    order.append(pumps)
    print(order)
    #subtotal:.2f means it will have 2 decimal places
    print(f"subtotal: ${subtotal:.2f}")

    #if not(popcorn=="n" and drink=="n".....
    #if popcorn!="n" and drink!="n" and candy!="n":
    # the keyword in checks if item on left is in sequence on right
    if not("n" in order):
        subtotal -= 1.50
        #order+="\ty discount\n"
        order.append("y")
    else:
        #order+="\tn discount\n"
        order.append("n")
        pass #pass by this line of code

    #order+=f"\n\tsubtotal: ${subtotal:.2f}\n"
    #order+=f"\ttax:     ${subtotal*.07:.2f}\n"
    #subtotal*=1.07
    #order+=f"\ttotal:   ${subtotal:.2f}\n"

    receipt =f'''
    User's Order:
        {order[0]} popcorn
        {order[1]} drink
        {order[2]} candy
        {order[3]} pumps
        {order[4]} discount
    '''
    print(receipt)
    completeorder.append(f'''
        {order[0]} popcorn
        {order[1]} drink
        {order[2]} candy
        {order[3]} pumps
        {order[4]} discount''')
    ui=input("Checkout? (type out checkout)")
    
print(f'''
Order total:    
    {"\n".join(completeorder)}
    
subtotal ${subtotal:.2f}
tax      ${subtotal*0.07:.2f}
total    ${subtotal*1.07:.2f}
''')




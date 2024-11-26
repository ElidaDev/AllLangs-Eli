#Iteration 1: Order some popcorn
subtotal = 0

items = []
loop = True
while loop:
    print(f''' 
    If you do not want an item type '4' 

    Select the number below the option you would like...      


             Popcorn sizes
        Small |  Medium |  Large
        (1)   |   (2)   |   (3)
        $5    |  $6     |  $7


    ''')

    size = input("Select a size for popcorn: ")

    if size == "1":
        subtotal += 5
        items.append("Small popcorn: $5")
    elif size == "2":
        subtotal += 6
        items.append("Medium popcorn: $6")
    elif size == "3":
        subtotal += 7
        items.append("Large popcorn: $7")
    else:
        print("No popcorn selected...")
        loop = False

#Iteration 2: Ordering a nice fresh soda pop
loop = True
while loop:
    print(f''' 
    If you do not want an item type '4' 

    Select the number below the option you would like...      


              Drink sizes
        Small |  Medium |  Large 
        (1)   |   (2)   |   (3)
        $3    |  $4     |  $5
    ''')

    x = input("Select a drink size: ")
    if x == "1":
        subtotal += 3
        items.append("Small drink: $3")
    elif x == "2":
        subtotal += 4

        items.append("Medium drink: $4")
    elif x == "3":
        subtotal += 5
        x = input('''
    Would you like a child size drink for an additional 38 cents?
    1 for yes
    2 for no
                  ''')
        if x == "1":
            subtotal += .38
            items.append("Child drink: $5.38")
            print("Child size drink selected")
        else:
            items.append("Large drink: $5")
            print("Child size drink not selected...")
    else:
        print("No drink selected...")
        loop = False

#Iteration 3: Get your candy
loop = True
while loop:
    print(f''' 
    If you do not want an item type '4' 

    Select the number below the option you would like...      


                Candy 
        Sour Patches |  M&Ms    |  Skittles
        (1)          |   (2)    |   (3)
        $2           |   $2.50  |   $2.50


    ''')

    size = input("Select a type of candy: ")

    if size == "1":
        subtotal += 2
        items.append("Sour patch kids: $2")
    elif size == "2":
        subtotal += 2.5
        x = input('''
                        M&Ms 
            Plain  | Peanuts    |  Crunchy
            (1)    |   (2)      |   (3)

        ''')
        if x == "1":
            items.append("Regular M&Ms: $2.50")
        elif x == "2":
            items.append("Peanuts M&Ms: $2.50")
        else:
            items.append("Crunchy M&Ms: $2.50")
    elif size == "3":
        subtotal += 2.5
        x = input('''
                        Skittles 
            Regular| Berry      |  Sour
            (1)    |   (2)      |   (3)

        ''')
        if x == "1":
            items.append("Regular Skittles: $2.50")
        elif x == "2":
            items.append("Berry Skittles: $2.50")
        else:
            items.append("Sour Skittles: $2.50")
    else:
        print("No candy selected.")
        loop = False
#Iteration 4: Butter topping
while True:
    try:
        x = int(input("How many pumps of butter do you need? "))
        if x >= 0:
            break
        else:
            x = 0
            break
    except ValueError:
        print("Please insert an integer value! ")

subtotal += x*.25
discount = 0

# Check for popcorn, a drink, and candy in the list.

if (any("popcorn" in item for item in items) and any("drink" in item for item in items)) and (any("skittles" in item.lower() for item in items) or any("m&ms" in item.lower() for item in items) or any("kids" in item.lower() for item in items)):
    discount += 1.50
else: 
    discount = 0
 
# Add a pump of butter to the list for each pump
for i in range(x):
    items.append("Pump of butter: $0.25")


print("")
print("\n".join(items))
print("")

print(f"Discount: {discount:.2f}")

taxtotal = subtotal * 1.07
taxtotal = taxtotal - subtotal
total = taxtotal + subtotal - discount
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: {taxtotal}")
print(f"Total: {total}")

    #import section

    #global var

    '''
        mode is what are you doing with the file?
            r - reading
            w - writing
            a - appending
            w+ - create and write
    '''


    #f(x)
    #csv - comma separated values
username = input("Input the username: ")
password = input("Input the password: ")


if password == "Password" and username == "Admin":
    def display_list():
        print()
        #read in the text file
        #with openTool(Filename,mode) as alias
        with open("TheList.csv","r") as file:
            #output to the terminal the data
            for eachLine in file:
                #print eachLine without \n on right end
                print(eachLine.rstrip())

    #print out how many coal and toys we need
    def count_items():
        toys,coal=0,0
        #read the text file
        with open("TheList.csv","r") as file:
            for eachLine in file:
                #look at 2nd piece of data
                #two var = eachLine w/0 \n are split based on", "
                name,gift = eachLine.rstrip().split(", ")
                data = eachLine.rstrip().split(", ")
                #add to toys or coal if that value present
                if gift == "toy":
                    toys+=1
                else:
                    coal+=1
                #puke results to terminal
            print(f"""
        Toys: {toys}
        Coal: {coal}
            """)

    def add_to_list():
        name = input("Name: ")
        gift = input("toy or coal ").lower()

        #open TheList.csv by appending to it alias is file
        with open("TheList.csv","a") as file:
            lineToWrite = f"{name}, {gift}\n"

            #file write this string
            file.write(lineToWrite)
            print(f"{name} was added!")

    def change_name():
        #obtain the old name and new name
        old = input("Current name: ")
        new = input("New name: ")

        #read in all the data aka save the file to a list
        with open("TheList.csv","r") as file:
            lines = file.readlines() #converts file to list
        #find the old name
        for i in range(len(lines)):
            name,gift = lines[i].strip().split(", ")
            if name == old:
                name = new
                newData = f"{name}, {gift}\n"
                lines[i] = newData
        print(lines) 
        #reset the old to the new aka overwrite the file
        with open("TheList.csv","w") as file:
            for eachLine in lines:
                file.write(eachLine)
                
    def change_gift():
        #obtain the old name and new name
        gname = input("Name: ")
        newgift = input("New gift: ")

        #read in all the data aka save the file to a list
        with open("TheList.csv","r") as file:
            lines = file.readlines() #converts file to list
        #find the old name
        for i in range(len(lines)):
            name,gift = lines[i].strip().split(", ")
            if name == gname:
                gift = newgift
                newData = f"{name}, {gift}\n"
                lines[i] = newData
        print(lines) 
        #reset the old to the new aka overwrite the file
        with open("TheList.csv","w") as file:
            for eachLine in lines:
                file.write(eachLine)

    def filter_gift():
        #obtain the old name and new name
        giftf = input("Gift to filter for: ")

        #read in all the data aka save the file to a list
        with open("TheList.csv","r") as file:
            lines = file.readlines() #converts file to list
        #find the old name
        for i in range(len(lines)):
            name,gift = lines[i].strip().split(", ")
            if gift == giftf:
                print(lines) 

    '''
        Dictionary similar to json
            "keyword" is associated with value
            [0,1,2,3,4]
            {"0":command,"1":command1,"2":command2}

    '''
    def invalid_choice():
        print("Invalid choice. Please select a valid option")

    def exit():
        print("Goodbye!")
        raise SystemExit  #stops the program

    options = {
            "display":display_list,
            "2":add_to_list,
            "3":count_items,
            "4":change_name,
            "5":change_gift,
            "6":filter_gift,
            "7":exit
            }

    #main loop
    while True:
        print("\n--- Santa's Nice and Naughty List ---")
        print("1. Display the list")
        print("2. Add a person to the list")
        print("3. Count toys and coal")
        print("4. Change name")
        print("5. Change gift")
        print("6. Find people with a gift")
        print("7. Exit")
        choice = input("Choose an option (1-7): ").strip()
                                        
        #dictionary.getChoice and if invalid run other command                                    
        action = options.get(choice,invalid_choice)
        action()

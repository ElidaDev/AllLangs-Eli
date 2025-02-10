for i in range(10):
    number = int(f"{i}0")
    grid = ("")
    while number <= 100:
        if number == 0:
            grid+=(f"00 ")
        else:
            grid+=(f"{number} ")
        number+=11
    print (grid)
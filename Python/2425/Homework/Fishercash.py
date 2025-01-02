coins = [0, 0, 0, 0]
cash = 0
total = 5
given = 40.43

def cword (coin, count):
    if coin != "Penny":    
        if count == 0:
            return ""
        elif count == 1:
            return f"1 {coin}"
        else:
            return f"{count} {coin}s"
    else:
        if count == 0:
            return ""
        elif count == 1:
            return f"1 {coin}"
        else:
            return f"{count} Pennies"

change = round((given - total)*100, 4)

print(change)
while change > 0:
    if change >= 100:
        cash += 1
        change -= 100
    elif change >= 25:
        coins[0] += 1
        change -= 25
    elif change >= 10:
        coins[1] += 1
        change -= 10
    elif change >= 5:
        coins[2] += 1
        change -= 5
    elif change >= 1:
        coins[3] += 1
        change -= 1
print(f"${cash}")
print(cword("Quarter", coins[0]), cword("Dime", coins[1]), cword("Nickel", coins[2]), cword("Penny", coins[3]))

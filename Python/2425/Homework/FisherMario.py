height = int(input("Enter the height: "))
for i in range(1, height + 1):
    left = ' ' * (height - i) + '#' * i
    right = '#' * i + ' ' * (height - i)    
    print(left + "  " + right)

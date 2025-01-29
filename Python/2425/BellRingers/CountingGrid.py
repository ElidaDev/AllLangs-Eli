for i in range(100):
    if i % 10 == 0 and i != 0:
        print()
    print(str(i).zfill(2), end= " ")
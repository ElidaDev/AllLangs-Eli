usersFavoriteSoda = input("What's your favorite soda? ")

for i in range(99,2,-1):
    print (f'''
{i} bottles of {usersFavoriteSoda} on the wall, {i} bottles of {usersFavoriteSoda}.
Take one down pass it around, {i-1} bottles of {usersFavoriteSoda} on the wall.''')
print(f'''
1 bottle of {usersFavoriteSoda} on the wall, 1 bottle of {usersFavoriteSoda}.
Take one down pass it around, no more bottles of {usersFavoriteSoda} on the wall.

No more bottles of {usersFavoriteSoda} on the wall, no more bottles of {usersFavoriteSoda}.
Go to the store and buy some more, 99 bottles of {usersFavoriteSoda} on the wall.
''')

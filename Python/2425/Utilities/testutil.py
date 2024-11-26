animals = ["Cow", "Pig", "Chicken", "Lion","Cat","Dog","Horse","Duck","Mouse","Devin","Johanna","Riley", "Issac","Eli","MaineCoon", "Ohio"]
sounds = ["Moo", "Oink", "Quack", "Rawr","Meow","Woof","Nae", "Quack", "Squeek","Sigma", "Idk","Hello my name is Riley Edwards","Skibidi","AHHH","Meow(but big)","Only in ohio"]
print(len(animals))

animalsounds = []
for i in range(len(animals)):
    animalsounds.insert(0,f'''\twith a {sounds[i]}-{sounds[i]} here and a {sounds[i]}-{sounds[i]} there
    \there a {sounds[i]}, there a {sounds[i]}, everywhere a {sounds[i]}-{sounds[i]}\n''')
    print(f'''
    Old MacDonald had a farm, E-I-E-I-O
    And on that farm he had a {animals[i]}, E-I-E-I-O
    {"".join(animalsounds)}''') 
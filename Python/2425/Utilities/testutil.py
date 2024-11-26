vowels = ['a', 'e', 'i', 'o', 'u']
line_1 = "I like to eat, eat, eat, apples and bananas"
word = "eat"
line_2 = "I like to {word}, {word}, {word}, {vowel}pples and b{vowel}n{vowel}n{vowel}s"
print(f"{line_1}\n{line_1}")
for vowel in vowels:
    if vowel == "a":
        word = "ate"
    elif vowel == "e":
        word = "eet"
    else:
        word = f"{vowel}te"
    print()
    print(line_2.format(vowel=vowel,word=word))
    print(line_2.format(vowel=vowel,word=word))
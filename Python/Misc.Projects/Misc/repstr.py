torep = input("What to replace (First, Last, Bnglish): ")
letter = input("What letter to replace it with: ")
string = input("Give the sentence to replace: ")

if torep == "First":
    words = string.split()
    modified_words = [letter + word[1:] for word in words]
    modified_string = ' '.join(modified_words)
    print(modified_string)
elif torep == "Last":
    words = string.split()
    modified_words = [word[:-1] + letter for word in words]
    modified_string = ' '.join(modified_words)
    print(modified_string)
elif torep == "Bnglish":
    words = string.split()
    modified_words = [letter + word[1:] if len(word) > 2 else letter + word for word in words]
    modified_string = ' '.join(modified_words)
    print(modified_string)
else:
    print("Invalid option for replacement.")
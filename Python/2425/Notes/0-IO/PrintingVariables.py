print("We're printing some stuff")

# The ""'s represent a String data type

# Anytime you run the input() function the data from the user is a string

name = input("What is your name? ")

print(name)

'''
    Vocab Words
    Abstraction - Removing complecity
    Algorithms  - Set of instructions
    Concatenation - Joining data together

'''

print("Why hello " + name)


# print(f-String)

print(f"Why hello {name}!")

output = f"Why hello {name}!"
print(output)

story = f'''
    This is a crazy story... 
    A long long time ago...
    {name} said something important.
'''

print(story)

time = input(f"What time did {name} wake up? ")

# concatenating a string to a previous variable

story += " "*4 + f"{name} woke up at {time}!"

print(story)

''' 
    Escape characters
    \\n = newline
    \\t = tab
    \\  = \\ 
'''

def twoSum(nums, target):
    for i in range(len (nums)){
        for j in range(len (nums)){
            if nums[i] + nums[j] == target:
                return [i,j]
            j+=1
        }
        i += 1
    }

nums = [2,7,11,15]
target = 9
#[0,1]
print(twoSum(nums,target))

nums = [3,2,4]
target = 6
#[1,2]
print(twoSum(nums,target))

nums = [3,3]
target = 6
#[0,1]
print(twoSum(nums,target))

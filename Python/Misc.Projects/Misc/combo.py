import random

# Generate a random 4-digit combination
def generate_combination():
    return ''.join(str(random.randint(0, 9)) for _ in range(4))

# Set the combination (change this to your desired combination)
combination = generate_combination()

# Attempt to unlock the combination lock
def unlock_combination_lock():
    attempts = 0
    while True:
        guess = input("Enter a 4-digit combination: ")
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue

        attempts += 1

        if guess == combination:
            print(f"Congratulations! You unlocked the combination lock in {attempts} attempts.")
            break
        else:
            print("Incorrect combination. Try again.")

if __name__ == '__main__':
    print("Welcome to the 4-Digit Combination Lock Simulator")
    print(f"Set the combination to: ????")
    unlock_combination_lock()
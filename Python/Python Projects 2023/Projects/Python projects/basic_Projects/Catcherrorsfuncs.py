def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def get_str_input(prompt):
    while True:
        try:
            value = str(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid String.")
def get_bool_input(prompt):
    while True:
        try:
            value = bool(input(prompt))
            return value
        except NameError:
            print("Invalid input. Please enter a valid input 'True' or 'False'. (Case sensitive)")
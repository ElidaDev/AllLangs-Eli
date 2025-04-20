# Prompt the user to input the format string
format_string = input("Enter format string (e.g., 'Format: nLog_base(x) sign mLog_base(y) = z'): ")

# Remove the leading "Format:" if present
if format_string.startswith("Format: "):
    format_string = format_string[len("Format: "):]

# Split the string by whitespace
tokens = format_string.split()

# Initialize variables
n = base = x = sign = m = y = z = None

# Loop through tokens to extract values
for token in tokens:
    # Check for tokens that include the log expression
    if "Log" in token:
        # Example token: "nLog_base(x)"
        coeff = token[0]  # The first character is the coefficient (n or m)
        underscore_index = token.find('_')
        paren_start = token.find('(')
        paren_end = token.find(')')
        base_val = token[underscore_index+1:paren_start]  # extract base
        arg_val = token[paren_start+1:paren_end]            # extract argument inside parentheses

        # For the first log expression, assign to n, base, and x.
        # For the second, assign to m and y.
        if n is None:
            n = coeff
            base = base_val
            x = arg_val
        else:
            m = coeff
            y = arg_val
    # Identify the sign (+ or -)
    elif token in ['+', '-']:
        sign = token
    # Skip the equals sign
    elif token == '=':
        continue
    # Otherwise, assign the token to z (the result)
    else:
        z = token

# Output the extracted values
print("n =", n)
print("base =", base)
print("x =", x)
print("sign =", sign)
print("m =", m)
print("y =", y)
print("z =", z)

import random

# letters, numbers and symbols lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# ask for the number of letters, numbers and symbols
letters_len = int(input("How many letter would you like?\n"))
numbers_len = int(input("How many numbers would you like?\n"))
symbols_len = int(input("How many symbols would you like?\n"))

# generate random letters, numbers and symbols of user given lenght
random_letters = [random.choice(letters) for _ in range(letters_len)]
random_numbers = [random.choice(numbers) for _ in range(numbers_len)]
random_symbols = [random.choice(symbols) for _ in range(symbols_len)]

# combine to generate ordered random password
ordered_password = random_letters + random_numbers + random_symbols

# make ordered password unordered random password
random.shuffle(ordered_password)
pswd = ''.join(ordered_password)

# Print the final password
print("Here is your password: " + pswd)
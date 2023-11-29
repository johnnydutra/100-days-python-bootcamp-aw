import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

letters_qty = int(input("How many letters would you like in your password?\n"))
symbols_qty = int(input("How many symbols would you like?\n"))
numbers_qty = int(input("How many numbers would you like?\n"))

password = ""
password_chars = []

# for l in range(0, letters_qty):
#   password += random.choice(letters)
for l in range(0, letters_qty):
  password_chars.append(random.choice(letters))

# for s in range(0, symbols_qty):
#   password += random.choice(symbols)
for s in range(0, symbols_qty):
  password_chars.append(random.choice(symbols))

# for n in range(0, numbers_qty):
#   password += random.choice(numbers)
for n in range(0, numbers_qty):
  password_chars.append(random.choice(numbers))

# for char in range(0, len(password_chars)):
#   selection_value = random.choice(password_chars)
#   selection_index = password_chars.index(selection_value)

#   password += selection_value
#   password_chars.pop(selection_index)

random.shuffle(password_chars)

for char in password_chars:
  password += char

print("Here is your password: " + password)
import random

names_string = input("Input party members' names: ")
names = names_string.split(", ")

random_number = random.randint(0, len(names) - 1)
print(f"{names[random_number]} gets to pay the bill")
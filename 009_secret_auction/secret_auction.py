from art import logo
import os

print(logo)
print("Welcome to the secret auction program.")

bids = {}
taking_bids = True

highest = -1
winner = ""
should_continue = "yes"

while taking_bids:
  name = input("What is your name? ")
  price = int(input("What is your bid? $"))
  bids[name] = price  
  
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if should_continue == "no":
    taking_bids = False
  elif should_continue == "yes":
    os.system('clear')

for bid in bids:
  if bids[bid] > highest:
    highest = bids[bid]
    winner = bid

print(f"The winner is {winner} with a bid of ${highest}")
import random
import rps_art

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if user_choice == 0:
  print(rps_art.rock)
elif user_choice == 1:
  print(rps_art.paper)
elif user_choice == 2:
  print(rps_art.scissors)

print("Computer chose:")

if computer_choice == 0:
  print(rps_art.rock)
elif computer_choice == 1:
  print(rps_art.paper)
elif computer_choice == 2:
  print(rps_art.scissors)

if user_choice == computer_choice:
  print("It's a draw.")
elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
  print("You lose!")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
  print("YOU WIN!")
else:
  print("You typed an invalid number. You lose!")
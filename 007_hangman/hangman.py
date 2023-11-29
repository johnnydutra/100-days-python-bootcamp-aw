import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f"The solution is: {chosen_word}")

display = []

for letter in chosen_word:
  display.append("_")

end_of_game = False

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = guess

  print(display)

  if "_" not in display:
    end_of_game = True
    print("You win!")
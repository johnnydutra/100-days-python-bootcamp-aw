import random, hangman_words
from hangman_art import logo, stages

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
display = []
end_of_game = False

print(logo)

for letter in chosen_word:
  display.append("_")

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  
  if guess in display:
    print(f"You've already guessed \"{guess}\"")

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = guess

  if guess not in chosen_word:
    lives -= 1
    print(f"You guessed \"{guess}\", that's not in the word. You lose a life.")
    if lives == 0:
      end_of_game = True
      print("You lose.")

  print(display)

  if "_" not in display:
    end_of_game = True
    print("You win!")
  
  print(stages[lives])
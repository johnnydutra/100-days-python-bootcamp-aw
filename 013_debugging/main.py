def my_function():
  for i in range(1, 21): # instead of 20
    if i == 20:
      print("You got it!")

my_function()

###

from random import randint
dice_imgs = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(0, 5) # instead of (1, 6)
print(dice_imgs[dice_num])

###

year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994: # instead of >
  print("You are a Gen Z.")

###

age = int(input("How old are you?")) # added casting
if age > 18:
  print(f"You can drive at age {age}")

###

pages = 0
words_per_page = 0
pages = int(input("Number of pages: "))
words_per_page = int(input("Number of words per page: ")) # instead of ==
total_words = pages * words_per_page
print(total_words)

###

def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) # added tab
  print(b_list)
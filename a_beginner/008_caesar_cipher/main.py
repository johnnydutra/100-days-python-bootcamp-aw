def greet():
  print("Hello")
  print("How do you do?")
  print("Isn't the weather nice today?")
greet()

def greet_with_name(name):
  print(f"Hello {name}")
  print("How do you do?")

greet_with_name("Angela")

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

greet_with("Angela", "England")
greet_with(location="England", name="Angela")
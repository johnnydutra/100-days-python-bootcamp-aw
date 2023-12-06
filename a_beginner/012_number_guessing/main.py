enemies = 1

def increase_enemies():
  global enemies
  enemies += 1
  print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

PI = 3.14159
URL = "https://www.google.com"
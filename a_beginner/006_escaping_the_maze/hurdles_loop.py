def move():
  print("Moving forward")

def turn_left():
  print("Turning left")

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()
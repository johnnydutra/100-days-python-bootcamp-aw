from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [100, 60, 20, -20, -60, -100]
field = []

for index in range(0, 6):
    racer = Turtle(shape="turtle")
    racer.penup()
    racer.color(colors[index])
    racer.goto(x=-220, y=y_positions[index])
    field.append(racer)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in field:
        if (turtle.xcor() > 220):
            is_race_on = False
            winner = turtle.pencolor()
            if (winner == user_bet):
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)





screen.exitonclick()
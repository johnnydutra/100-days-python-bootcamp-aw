import turtle as t
import random

bela = t.Turtle()
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "violet", "magenta", "black"]
directions = [0, 90, 180, 270]

# for _ in range(4):
#     bela.forward(100)
#     bela.right(90)

# for _ in range(15):
#     bela.forward(10)
#     bela.penup()
#     bela.forward(10)
#     bela.pendown()

# def draw_shape(sides, color):
#     for _ in range(sides):
#         angle = 360 / sides
#         bela.color(color)
#         bela.forward(100)
#         bela.right(angle)

# for sides in range(3, 11):
#     color = random.choice(colors)
#     draw_shape(sides, color)

# bela.pensize(15)
bela.speed("fastest")
# for _ in range(200):
#     bela.color(random.choice(colors))
#     bela.forward(30)
#     bela.setheading(random.choice(directions))

t.colormode(255)
def generate_random_rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return(r, g, b)

# for _ in range(200):
#     bela.color(generate_random_rgb_color())
#     bela.forward(30)
#     bela.setheading(random.choice(directions))

def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        bela.color(generate_random_rgb_color())
        bela.circle(100)
        bela.setheading(bela.heading() + 10)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
import colorgram, random, turtle

# colors = colorgram.extract("C:\Coding\\100-days-python-bootcamp-aw\\b_intermediate\\018_hirst_painting\painting.jpg", 25)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(248, 248, 246), (241, 249, 246), (250, 244, 248), (241, 245, 249), (4, 14, 31), (214, 132, 111), (53, 26, 18), (18, 104, 155), (148, 83, 
45), (240, 213, 73), (215, 87, 65), (164, 163, 34), (156, 9, 28), (155, 63, 100), (178, 136, 158), (204, 76, 104), (12, 63, 34), (92, 8, 21), (14, 94, 54), (10, 176, 215), (4, 62, 143), (20, 134, 84), (152, 28, 20), (11, 208, 199), (145, 225, 213)]

turtle.colormode(255)
tim = turtle.Turtle()

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.speed("fastest")

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
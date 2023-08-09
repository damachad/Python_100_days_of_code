import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
# Color list obtained using cologram.py to extract colors from a picture of one of Alex Hirst paintings
color_list = [(187, 69, 34), (19, 96, 163), (140, 46, 86), (219, 236, 234), (243, 219, 227), (251, 158, 59), (250, 206, 0), (190, 87, 120), (209, 129, 178), (207, 215, 74), (1, 88, 80), (2, 195, 96), (3, 130, 88), (2, 162, 201), (60, 37, 83), (166, 28, 78), (60, 37, 81), (244, 79, 15), (127, 166, 193), (65, 43, 89), (120, 188, 160), (220, 173, 193), (149, 215, 184)]

tim = Turtle()
tim.speed("fastest")
tim.penup()
x = -230.00
y = -220.00
tim.goto(x, y)
tim.pensize(20)
tim.hideturtle()

up_line = 50
for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.goto(x, y + up_line)
    up_line += 50

screen = Screen()
screen.exitonclick()

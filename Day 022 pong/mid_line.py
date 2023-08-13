from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.pensize(10)
        self.hideturtle()
        self.goto(x=0, y=-300)
        self.setheading(90)

    def draw_line(self):
        while self.ycor() < 300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(30)

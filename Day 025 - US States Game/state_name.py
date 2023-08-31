from turtle import Turtle


class StateName(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(arg=state)


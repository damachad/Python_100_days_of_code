from turtle import Turtle
START_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(START_POSITION)
        self.setheading(90)

    def move_up(self):
        self.forward(20)

    def reset_pos(self):
        self.goto(START_POSITION)

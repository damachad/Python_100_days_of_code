from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(x=x_cor, y=y_cor)

    def move_up(self):
        new_y = self.ycor() + 30
        if new_y < 260:
            self.goto(self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        if new_y > -250:
            self.goto(self.xcor(), y=new_y)

from turtle import Turtle
FONT = ("Courier", 60, "bold")


class Score(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=xcor, y=ycor)
        self.score = 0
        self.write(arg=self.score, font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        if self.score > 3:
            self.color("red")
        self.write(arg=self.score, font=FONT)

    def game_over(self):
        self.color("white")
        self.goto(x=-215, y=-50)
        self.write(arg="Game Over!", font=FONT)

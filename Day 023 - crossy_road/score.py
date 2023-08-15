from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-275, y=260)
        self.level = 1
        self.write(arg=f"Level: {self.level}", font=FONT)

    def update(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(x=-70, y=-10)
        self.write(arg="Game Over", font=FONT)

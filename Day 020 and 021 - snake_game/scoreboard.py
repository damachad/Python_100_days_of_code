from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGN, font=FONT)

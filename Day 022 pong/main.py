from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from mid_line import Line
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(x_cor=-350, y_cor=0)
r_paddle = Paddle(x_cor=350, y_cor=0)
ball = Ball()
score1 = Score(xcor=-75, ycor=210)
score2 = Score(xcor=30, ycor=210)
line = Line()
line.draw_line()

screen.listen()
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)

    # Detect collision with top and lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.xcor() > r_paddle.xcor() - 25 and ball.distance(r_paddle) < 50:
        ball.bounce_x()

    # Detect collision with l_paddle
    if ball.xcor() <= l_paddle.xcor() + 25 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Detect going past right 'goal'
    if ball.xcor() > 390:
        score1.update()
        ball.reset_pos()

    # Detect going past left 'goal'
    if ball.xcor() < -390:
        score2.update()
        ball.reset_pos()

    if score1.score == 5:
        game_on = False
        score1.game_over()
        print("Left-side player won!")

    if score2.score == 5:
        game_on = False
        score2.game_over()
        print("Right-side player won!")

screen.exitonclick()

from turtle import Screen
from player import Player
from score import Score
from CarManager import CarManager
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Crossy Road")

player = Player()
score = Score()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move_up, "Up")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    # Generate random moving cars  
    car_manager.create_cars()
    car_manager.move_cars()

    # Next level
    if player.ycor() > 280:
        player.reset_pos()
        score.update()
        car_manager.move_increment += 5

    # Collision with car
    for cars in car_manager.all_cars:
        if player.distance(cars) < 20:
            game_on = False
            score.game_over()

screen.exitonclick()

from turtle import Turtle
import random
colors = ["lime green", "red", "blue", "yellow", "green", "indigo", "pink", "coral"]
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_increment = MOVE_INCREMENT

    def create_cars(self):
        chance = random.randint(1, 10)
        if chance > 8:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(colors))
            car.goto(x=300, y=random.randint(-250, 250))
            car.setheading(180)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(5 + self.move_increment)


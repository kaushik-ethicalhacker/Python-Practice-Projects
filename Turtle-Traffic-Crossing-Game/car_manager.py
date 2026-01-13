from turtle import Turtle
import random

COLORS = ["red", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.CARS = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def spawn_new_car(self):
        random_index = random.randint(1, 6)
        if random_index == 1:
            t = Turtle()
            t.shape("square")
            t.shapesize(stretch_wid=1, stretch_len=2)
            t.penup()
            t.color(random.choice(COLORS))
            t.goto(300, random.randint(-250,230))
            self.CARS.append(t)

    def move_cars(self):
        for car in self.CARS:
            new_x = car.xcor()-self.car_speed
            car.goto(new_x,car.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT







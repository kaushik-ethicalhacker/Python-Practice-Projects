import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Race Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

scoreboard.text()
player.start_pos()


screen.listen()
col =0
if col != 1:
    screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 280:
        player.start_pos()
        car_manager.level_up()
        scoreboard.score_up()
        scoreboard.text()


    car_manager.spawn_new_car()

    car_manager.move_cars()

    for car in car_manager.CARS:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()






screen.exitonclick()

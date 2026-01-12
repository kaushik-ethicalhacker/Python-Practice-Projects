from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Scoreboard

s = Screen()
s.bgcolor("black")
s.setup(width=600, height=600)
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

snake.create_snake()


s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)

    snake.move()

    if snake.TURTLES[0].distance(food) < 15:
        food.movee()
        snake.extend()
        scoreboard.increase_score()



    if snake.TURTLES[0].xcor() > 295 or snake.TURTLES[0].xcor() < -295 or snake.TURTLES[0].ycor() > 295 or snake.TURTLES[0].ycor() < -295:
        scoreboard.game_over()
        game_is_on = False

    for collision in snake.TURTLES[1:]:
        if snake.head.distance(collision) < 15:
            game_is_on = False
            scoreboard.game_over()

s.exitonclick()
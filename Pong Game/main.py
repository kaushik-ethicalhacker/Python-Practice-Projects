from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Pong Game")
s.tracer(0)


paddle = Paddle()
ball = Ball()
score = Score()

paddle.paddles()



s.listen()
s.onkey(paddle.go_upr,"Up")
s.onkey(paddle.go_downr,"Down")
s.onkey(paddle.go_upl,"w")
s.onkey(paddle.go_downl,"s")

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(ball.move_speed)

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if (ball.distance(paddle.PADDLES[0])<50 and ball.xcor() > 320 or
        ball.distance(paddle.PADDLES[1])< 50  and  ball.xcor() < -320):
         ball.bounce_x()

    if ball.xcor() > 380:
        ball.setposition(0,0)
        ball.bounce_x()
        score.r_scoree()
        ball.move_speed =0.1

    if ball.xcor() < -380:
        ball.setposition(0,0)
        ball.bounce_y()
        ball.bounce_x()
        score.l_scoree()
        ball.move_speed =0.1




















s.exitonclick()
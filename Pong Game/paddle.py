from turtle import Turtle
MOVE_DISTANCE = 30

class Paddle:
    def __init__(self):
        self.PADDLES = []




    def paddles(self):
        pos = [(350,0),(-350,0)]
        for paddless in pos:
            t= Turtle()
            t.shape("square")
            t.shapesize(stretch_wid=5, stretch_len=1)
            t.color("white")
            t.penup()
            t.goto(paddless)
            self.PADDLES.append(t)

    def go_upr(self):
        new_y = self.PADDLES[0].ycor() +MOVE_DISTANCE
        self.PADDLES[0].goto(self.PADDLES[0].xcor(),new_y)

    def go_downr(self):
        new_y = self.PADDLES[0].ycor() -MOVE_DISTANCE
        self.PADDLES[0].goto(self.PADDLES[0].xcor(),new_y)

    def go_upl(self):
        new_y = self.PADDLES[1].ycor() +MOVE_DISTANCE
        self.PADDLES[1].goto(self.PADDLES[1].xcor(),new_y)

    def go_downl(self):
        new_y = self.PADDLES[1].ycor() -MOVE_DISTANCE
        self.PADDLES[1].goto(self.PADDLES[1].xcor(),new_y)



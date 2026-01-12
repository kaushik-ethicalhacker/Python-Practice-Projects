from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.xm = 10
        self.ym = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor()+self.xm
        new_y = self.ycor()+self.ym
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.ym *= -1
        self.move_speed *= 0.9
    def bounce_x(self):
        self.xm *= -1
        self.move_speed *= 0.9
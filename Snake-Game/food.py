from turtle import Turtle
import random as rd


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.speed(1000)
        self.movee()

    def movee(self):
        self.goto(rd.randint(-260,260), rd.randint(-260,260))



from turtle import Turtle
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.TURTLES =[]
        self.create_snake()
        self.head = self.TURTLES[0]



    def create_snake(self):
        x = 0
        for  new in range(2):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            t.setpos(x, 0)
            t.color("white")
            self.TURTLES.append(t)
            x -= 20


    def extend(self):
        for new in range(1):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            t.setpos(self.TURTLES[-1].pos())
            t.color("white")
            self.TURTLES.append(t)





    def move(self):
        for move in range(len(self.TURTLES) - 1, 0, -1):
            new_x = self.TURTLES[move - 1].xcor()
            new_y = self.TURTLES[move - 1].ycor()
            self.TURTLES[move].goto(new_x, new_y)
        self.TURTLES[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.TURTLES[0].heading() != 270 :
            self.TURTLES[0].setheading(90)


    def down(self):
        if self.TURTLES[0].heading() != 90:
            self.TURTLES[0].setheading(270)


    def left(self):
        if self.TURTLES[0].heading() != 0 :
            self.TURTLES[0].setheading(180)


    def right(self):
        if self.TURTLES[0].heading() != 180:
            self.TURTLES[0].setheading(0)




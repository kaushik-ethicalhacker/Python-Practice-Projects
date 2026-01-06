import turtle as t
import random as rd
import image as im

t.colormode(255)
t.speed(25)
y=-150
for i in range(10):
    t.teleport(-150,y)
    for j in range(10):
        c = rd.randint(0, len(im.col) - 1)
        t.hideturtle()
        t.penup()
        t.dot(20, im.col[c])
        t.fd(50)
        y+=5




screen = t.Screen()
screen.exitonclick()
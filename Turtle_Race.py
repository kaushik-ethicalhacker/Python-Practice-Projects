import random
from turtle import Turtle,Screen
s = Screen()

s.setup(width=500,height=400)
bet = s.textinput(title="Make your bet", prompt="What turtle will win the game?").lower()

race_start = 0

colors = ["red","blue","green","black","orange","pink"]

all_turtles = []

x = -230
y = -100
for turtle in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x,y)
    y += 40
    all_turtles.append(new_turtle)

if bet:
    race_start = 1


while race_start:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            winning_turtle = turtle.pencolor()
            if winning_turtle == bet:
                print(f"You win!, The winner is {winning_turtle} turtle.")
            else:
                print(f"You lose :( , The winner is {winning_turtle} turtle.")
            race_start = 0
        turtle.forward(random.randint(1,10))



s.exitonclick()
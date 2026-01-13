from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-210, 250)


    def text(self):
        self.clear()
        self.color("black")
        self.goto(-210, 250)
        self.write(f"Level:{self.score} ", align="center", font=FONT)

    def score_up(self):
        self.score += 1

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
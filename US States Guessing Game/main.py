import turtle as t
import time
import pandas as pd

ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")

df = pd.read_csv("50_states.csv")

turtle = t.Turtle()
screen = t.Screen()
screen.title("U.S. States Game Start")

image = "blank_states_img.gif"

screen.bgpic(image)
screen.setup(width = 725, height=600)
screen.tracer(0)

title = "Guess the States"
answered = 0

answer = screen.textinput(title = title, prompt = "Enter a state's name").lower()
guessed_states = []

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    lower = df["state"].str.lower()

    if answer == "exit":
        missing_states = []
        for state in df["state"]:
            if state not in guessed_states:
                missing_states.append(state)
        print(f"States which you didn't guess \n {pd.DataFrame(missing_states)}")
        game_is_on = False

    elif answered <= 50:
        if len(df[lower == answer]) == 1:
            row = df[lower == answer]
            x_cor = row["x"].iloc[0]
            y_cor = row["y"].iloc[0]

            turtle.hideturtle()
            turtle.penup()
            turtle.color("black")
            turtle.goto(x_cor, y_cor)
            turtle.write(row["state"].iloc[0], align=ALIGNMENT, font=FONT)
            guessed_states.append(row["state"].iloc[0])


            answered += 1
            title = f"{answered}/50 States Correct"
            answer = screen.textinput(title = title, prompt = "Enter another state's name").lower()


        else:
            answer = screen.textinput(title = title, prompt = "Enter a state's name").lower()

    else:
        game_is_on = False


screen.exitonclick()
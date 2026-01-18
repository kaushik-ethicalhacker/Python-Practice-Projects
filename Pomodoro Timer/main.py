import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)

    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)

    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)



# ---------------------------- TIMER MECHANISM ------------------------------- #
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text = "")
    global REPS
    REPS = 0






# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min= math.floor(count/60)
    count_sec = count%60

    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down,count -1)
    else:
        start_timer()
        marks= ""
        work_sessions = math.floor(count/60)
        for i in range(work_sessions):
            marks+="✓"
        check_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.configure(background=YELLOW)
window.config(padx=100, pady=50)




canvas = tk.Canvas(width=210, height=244, background=YELLOW, highlightthickness=0)
image_tomato = tk.PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=image_tomato)

timer_text = canvas.create_text(105,130,text="00:00", font=(FONT_NAME,35,"bold"), fill="white")
canvas.grid(row = 1, column = 1)


timer_label = tk.Label(text="Timer", font=(FONT_NAME,35,"bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row = 0, column = 1)



check_label = tk.Label(font=(FONT_NAME,15,"bold"),fg=GREEN, bg=YELLOW)
check_label.grid(row = 3, column = 1)


start_button = tk.Button(text="Start", command=start_timer,bg="white")
start_button.grid(row = 2, column = 0)

reset_button = tk.Button(text="Reset", command=reset_timer,bg="white")
reset_button.grid(row = 2, column = 2)





window.mainloop()












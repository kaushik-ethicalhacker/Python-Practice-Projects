import tkinter as tk
import data as d
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)


BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None

dataa = d.Data()
window = tk.Tk()

def flip_card():
    canvas.itemconfig(card_title,text ="English",fill="white")
    canvas.itemconfig(card_word,text =dataa.word_english(),fill="white")
    canvas.itemconfig(card, image=back_card)


def next_card():
    global flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=dataa.next_word(), fill="black")
    canvas.itemconfig(card, image=front_card)

    if dataa.next_word() != "Done!":
        flip_timer = window.after(3000, flip_card)



def is_known():
    dataa.save_progress()
    next_card()

window.title("Flashy")
window.configure(background=BACKGROUND_COLOR)
window.config(padx=50, pady=50)



canvas = tk.Canvas(width=800, height=526,background=BACKGROUND_COLOR, highlightthickness=0)
front_card = tk.PhotoImage(file="card_front.png")
back_card = tk.PhotoImage(file="card_back.png")
card= canvas.create_image(400, 263, image=front_card)
card_title= canvas.create_text(400,130,text="",font=("Arial", 40,"italic"))
card_word = canvas.create_text(400,280,text="",font=("Arial", 50,"bold"))
canvas.grid(row=0, column=0,columnspan=2)


wrong_image = tk.PhotoImage(file="wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = tk.PhotoImage(file="right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)


next_card()


window.mainloop()
from tkinter import *
import requests


import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)


def get_quote():
    quote = requests.get("https://api.kanye.rest/")
    if quote.status_code != 200:
        raise Exception("Error getting quote")
    quote_json = quote.json()
    canvas.itemconfig(quote_text,text =quote_json["quote"])




window = Tk()
window.title("Kanye Says...")
window.config(padx=100, pady=100)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 15, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()
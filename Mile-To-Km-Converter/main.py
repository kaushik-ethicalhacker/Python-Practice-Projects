import tkinter as tk
FONT=("Arial", 10,"bold")

window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)


end = tk.END

is_equal_to = tk.Label(text="is equal to",font= FONT)
is_equal_to.grid(row=1,column=0)

miles = tk.Label(text="Miles",font=FONT )
miles.grid(row=0,column=2)

miles_input = tk.Entry(width=10)
miles_input.insert(end,string = "0")

miles_input.grid(row=0,column=1)

kms = tk.Label(text="Km",font=FONT)
kms.grid(row=1,column=2)

km_label = tk.Label(text="0",font=FONT)
km_label.grid(row=1,column=1)


def button_clicked():
    mile = float(miles_input.get())
    km = str(round(mile * 1.609))
    km_label.config(text=km)

calculate = tk.Button(text="Calculate",command=button_clicked)
calculate.grid(row=2,column=1)


window.mainloop()

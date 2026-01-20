import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password = password_letters + password_symbols + password_numbers
    random.shuffle(password)

    passw = "".join(password)

    password_input.insert(0,passw)
    pyperclip.copy(passw)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():

    if len(website_input.get())==0 or len(password_input.get()) == 0  :
        messagebox.showinfo("Error","Please enter all fields")

    else:
        is_ok = messagebox.askokcancel(title = website_input.get(),message=f"These are the details of the website you entered:\n"
                                                          f"Email: {email_input.get()}\n"
                                                          f"Username: {email_input.get()}\n"
                                                          f"Password: {password_input.get()}"
                                                          f"Is it ok to save?",)
        if is_ok:
            with open("data.txt","a") as f:
                f.write(f"{website_input.get()} | {email_input.get()} | {password_input.get()}" )
                website_input.delete(0,"end")
                email_input.delete(0,"end")
                password_input.delete(0,"end")

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.configure(background="white",padx=80,pady=80)


canvas = tk.Canvas(background="white",width=200,height=200,highlightthickness=0)
image = tk.PhotoImage(file="logo.png")
canvas.create_image(140,100,image=image)
canvas.grid(row=0,column=1)

website_label = tk.Label(text="Website:",bg="white")
website_label.grid(row=1,column=0)

email_label = tk.Label(text="Email/Username:",bg="white",padx=10)
email_label.grid(row=2,column=0)

password_label = tk.Label(text="Password:",bg="white")
password_label.grid(row=3,column=0)


website_input = tk.Entry(width=50)
website_input.grid(row=1,column=1,columnspan=2)

email_input = tk.Entry(width=50)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"User@email.com")

password_input = tk.Entry(width=34)
password_input.grid(row=3,column=1)



generate_button = tk.Button(text="Generate Password",command=generate_password, bg="white",width=15,height=1,fg="black")
generate_button.grid(row=3,column=2)

add_button = tk.Button(text="Add",command=add,width=50,bg="white",fg="black",height=1)
add_button.grid(row=5,column=1,columnspan=2)




window.mainloop()

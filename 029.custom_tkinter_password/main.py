import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customtkinter
from random import choice, randint, shuffle
import pyperclip
from PIL import Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.insert(0, password)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(password) == 0 or len(website) == 0:
        messagebox.showwarning(title="Empty fields",
                               message="Plese fill out all fields")
    elif messagebox.askokcancel(title=website, message=f"You've entered: \nEmail: {email}\nPassword: {password}" f"\nIs it OK to save?"):
        with open("saved_passwords.txt", mode="a") as file:
            file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)

    print(website, email, password)


window = customtkinter.CTk()
window.title("Password Manager")
window.geometry("600x500")
window.minsize(670, 400)

# canvas = customtkinter.CTkCanvas(master=window, width=600, height=500)
canvas = customtkinter.CTkCanvas(
    master=window, width=250, height=250, bg="black")
logo_png = PhotoImage(master=window, file="lock.png")
canvas.create_image(125, 135, image=logo_png)
canvas.grid(row=1, column=1, columnspan="1")

title_label = customtkinter.CTkLabel(
    master=window, text='Password Manager', font=('Helvetica', 32))
title_label.grid(row=0, column=1, pady=20)

website_label = customtkinter.CTkLabel(
    master=window, text='Website:', width=200)
website_label.grid(row=2, column=0, sticky=tk.E)
username_label = customtkinter.CTkLabel(
    master=window, text='Email/Username:', width=200)
username_label.grid(row=3, column=0, sticky=tk.E)
password_label = customtkinter.CTkLabel(
    master=window, text='Password:', width=200)
password_label.grid(row=4, column=0, sticky=tk.E)

generate_button = customtkinter.CTkButton(
    master=window, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=3, padx=10)
add_button = customtkinter.CTkButton(master=window, text="Save", command=save)
add_button.grid(row=4, column=3, padx=10)


website_entry = customtkinter.CTkEntry(master=window,
                                       width=200,
                                       height=35,
                                       placeholder_text='Website',
                                       border_width=2,
                                       corner_radius=5)
website_entry.grid(row=2, column=1, pady=10)

email_entry = customtkinter.CTkEntry(master=window,
                                     width=200,
                                     height=35,
                                     placeholder_text='Username/Email',
                                     border_width=2,
                                     corner_radius=5)
email_entry.grid(row=3, column=1, pady=0)

password_entry = customtkinter.CTkEntry(master=window,
                                        width=200,
                                        height=35,
                                        placeholder_text='Password',
                                        border_width=2,
                                        corner_radius=5)
password_entry.grid(row=4, column=1, pady=10)


window.mainloop()

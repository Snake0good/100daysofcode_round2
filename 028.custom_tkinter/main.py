import customtkinter
import tkinter as tk
from tkinter import *
import math

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def break_timer():
    print("break")
    title_label.configure(text="Break")
    canvas.configure(bg='#0096c7')
    count_down(SHORT_BREAK_MIN * 60)


def start_timer():
    print("start")
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    title_label.configure(text="Work")
    canvas.configure(bg='#00ab41')
    count_down(work_sec)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


def reset_timer():
    canvas.configure(bg='#1d3557')
    window.after_cancel(timer)
    canvas.itemconfigure(timer_text, text="00:00")
    title_label.configure(text="Timer", font=(
        FONT_NAME, 50, "bold"))
    global reps
    reps = 0


# window = Tk()
window = customtkinter.CTk()
window.title("Pomodoro")
window.geometry("600x500")
window.minsize(600, 500)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure((0, 2), weight=1)


# canvas
canvas = customtkinter.CTkCanvas(
    master=window, width=500, height=250, bg='black')
tomato_png = PhotoImage(master=window, file="tomato.png")
canvas.create_image(250, 150, image=tomato_png)
timer_text = canvas.create_text(
    250, 30, text="00:00", fill="white", font=(FONT_NAME, 50, "bold"))
canvas.grid(column=0, row=0, columnspan=4)


# label
title_label = customtkinter.CTkLabel(
    master=window, text="Pomodoro Timer", anchor='n', font=('Times New Roman', 30))
# title_label.grid(column=1, row=0, sticky=N)
title_label.place(relx=0.5, rely=0, anchor='n')

# start_button = Button(text="Start", command=start_timer)
start_button = customtkinter.CTkButton(
    master=window, text="Start", command=start_timer)
start_button.grid(row=1, column=0, padx=20, pady=20)

# start_button = Button(text="Start", command=start_timer)
break_button = customtkinter.CTkButton(
    master=window, text="Break", command=break_timer, fg_color='#00ab41', hover_color='#008631')
break_button.grid(row=1, column=1, padx=10, pady=10)

reset_button = customtkinter.CTkButton(
    master=window, text="Reset", command=reset_timer)
reset_button.grid(row=1, column=2, padx=20, pady=20)

window.mainloop()

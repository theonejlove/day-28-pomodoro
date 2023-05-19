from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    countdown(1500)


def start_timer():
    global reps
    reps += 1

    work_sec= WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title.config(text="Break", fg=RED)
        countdown(long_break_sec)
        reps = 0
    elif reps % 2 == 0:
        title.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        title.config(text="Work", fg=GREEN)
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    count_min = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 12), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 12), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check = Label(bg=YELLOW, fg=GREEN)
check.grid(column=1, row=3)

window.mainloop()
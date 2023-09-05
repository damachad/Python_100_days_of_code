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
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    timer_label.config(text="Timer", fg=GREEN)
    reps = 0
    checkmark.config(text="")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps <= 8:
        if reps % 2 != 0:
            timer_label.config(text="Work", fg=GREEN)
            count_down(work_sec)
        elif reps == 8:
            timer_label.config(text="Break", fg=RED)
            count_down(long_break_sec)
        else:
            timer_label.config(text="Break", fg=PINK)
            count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


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
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(row=1, column=1)

# Labels
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 36, "bold"), bg=YELLOW)
timer_label.grid(row=0, column=1)

checkmark = Label(fg=GREEN, font=(FONT_NAME, 24, "bold"), bg=YELLOW)
checkmark.grid(row=3, column=1)

# Buttons

start_but = Button(text="Start", width=6, font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=start_timer)
start_but.grid(row=2, column=0)
reset_but = Button(text="Reset", width=6, font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=reset_timer)
reset_but.grid(row=2, column=2)

window.mainloop()

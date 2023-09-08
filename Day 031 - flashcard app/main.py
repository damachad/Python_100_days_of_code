from tkinter import *
import pandas
import random

# ------------------------ CONSTANTS ----------------------- #

BACKGROUND_COLOR = "#B1DDC6"
ORIGINAL_LANGUAGE = "French"
TRANSLATE_LANGUAGE = "English"
THINKING_INTERVAL = 3  # in seconds

# --------------------- CARD MECHANICS --------------------- #

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")

word_bank = df.to_dict(orient="records")


def generate_words():
    global testing_word, timer
    testing_word = random.choice(word_bank)
    window.after_cancel(timer)
    canvas.itemconfig(card, image=front_card)
    canvas.itemconfig(title, fill="black", text=ORIGINAL_LANGUAGE)
    canvas.itemconfig(word, text=testing_word[ORIGINAL_LANGUAGE], fill="black")
    timer = window.after(ms=THINKING_INTERVAL * 1000, func=flip_card)


def flip_card():
    canvas.itemconfig(card, image=back_card)
    canvas.itemconfig(title, fill="white", text=TRANSLATE_LANGUAGE)
    canvas.itemconfig(word, fill="white", text=testing_word[TRANSLATE_LANGUAGE])


def update_words():
    word_bank.remove(testing_word)
    words_to_learn = pandas.DataFrame(word_bank)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    generate_words()


# ---------------------- UI INTERFACE ---------------------- #

# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(ms=THINKING_INTERVAL * 1000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=front_card)
title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=generate_words)
wrong_button.grid(row=1, column=0)
check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=update_words)
right_button.grid(row=1, column=1)

generate_words()

window.mainloop()

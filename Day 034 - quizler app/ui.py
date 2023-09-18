from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0

        # Window
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="[Placeholder]",
                                                     fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        # Buttons
        self.cross = PhotoImage(file="images/false.png")
        self.check = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.check, bg=THEME_COLOR, highlightthickness=0,
                                   pady=20, padx=20, command=self.answer_true)
        self.right_button.grid(row=2, column=0)
        self.wrong_button = Button(image=self.cross, bg=THEME_COLOR, highlightthickness=0,
                                   pady=20, padx=20, command=self.answer_false)
        self.wrong_button.grid(row=2, column=1)

        # Labels
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR,
                                 pady=20, padx=20, font=("Arial", 14, "italic"), fg="white")
        self.score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)

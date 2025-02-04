from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        
        self.screen = Tk()
        self.screen.title("QuizzzzzzzzzzzzzE Timeeeeee!!")
        self.screen.minsize(width = 340, height = 500)
        self.screen.config(padx = 20, pady = 20, bg = THEME_COLOR)
        
        self.counter = 0
        self.label = Label(text=f"Score: {self.counter}", bg = THEME_COLOR, fg = "white", font=("Arial", 10))
        self.label.grid(row = 0, column = 1)
        
        self.canvas = Canvas(width = 300, height = 250, highlightthickness = 0, bd = 0)
        self.question = self.canvas.create_text(150, 120,
                                                width = 280,
                                                text="", 
                                                font=("Arial", 20, "italic")
                                                , fill=THEME_COLOR)
        self.canvas.grid(row = 1 , column = 0, columnspan = 2, pady = 50)
        
        correct_image = PhotoImage(file="Trivia_Quiz\\images\\true.png")
        wrong_image = PhotoImage(file="Trivia_Quiz\\images\\false.png")
        
        def next():
            if self.quiz.still_has_questions():
                self.canvas.config(bg = "White")
                self.new_question()
            else:
                self.canvas.itemconfig(self.question, text="Quiz Over!")
                self.correct_button.config(state="disabled")
                self.wrong_button.config(state="disabled")
        
        def correct_check():
            check = self.quiz.check_answer("True")
            give_feedback(check)
            
        def wrong_check():
            check = self.quiz.check_answer("False")
            give_feedback(check)        
                
        def give_feedback(is_correct):
            if is_correct:
                self.canvas.config(bg="green")
                self.counter += 1
            else:
                self.canvas.config(bg="red")

            self.label.config(text=f"Score: {self.counter}")

            self.screen.after(1000, next)
        
        correct = Button(image = correct_image, highlightthickness = 0, bd = 0, command = correct_check)
        correct.grid(row = 2, column = 0)
        wrong = Button(image = wrong_image, highlightthickness = 0, bd = 0, command = wrong_check)
        wrong.grid(row = 2, column = 1)
        
        self.new_question()
        
        self.screen.mainloop()
        
    def new_question(self):
        next_ques = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=next_ques)
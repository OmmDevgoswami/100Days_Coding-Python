import tkinter
from math_problem import MathProblem
from game import Game
from popup import Popup
 
 
def next_problem():
    """Generate a new math problem, and clear the entry fields."""
    problem.new_problem()
    num1_label["text"] = f"{problem.num1:5}"
    num2_label["text"] = f"+ {problem.num2:3}"
    thousands_value.set("")
    hundreds_value.set("")
    tens_value.set("")
    ones_value.set("")
    ones_entry.focus()
 
 
def check_answer():
    """Check the user's answer, and return True if it is correct."""
    user_answer = thousands_entry.get() + hundreds_entry.get() + tens_entry.get() + ones_entry.get()
    if user_answer.isdigit():
        return int(user_answer) == problem.answer
    else:
        return False
 
 
def end_game():
    """End the game, and save the user's score if they got the high score."""
    Popup("終わります", f"遊んでくれてありがとう!\nあなたのスコア：{game.score}")
    game.high_score_check()
    window.destroy()
 
 
def entry_validation(char):
    """Check the user input, and return True if it is a single digit, or a deletion."""
    if len(char) == 0:
        return True
    elif char.isdigit() and len(char) == 1:
        return True
    else:
        return False
 
 
# Event handlers
def ones_handler(event):
    """If a digit was entered, move focus to the tens digit entry field.
    If the Enter key was pressed, act as if the button was clicked."""
    if event.keysym == "Return":
        button_click()
    elif event.char.isdigit():
        tens_entry.focus()
 
 
def tens_handler(event):
    """If a digit was entered, move focus to the hundreds digit entry field.
    If the Enter key was pressed, act as if the button was clicked."""
    if event.keysym == "Return":
        button_click()
    elif event.char.isdigit():
        hundreds_entry.focus()
 
 
def hundreds_handler(event):
    """If a digit was entered, move focus to the thousands digit entry field.
    If the Enter key was pressed, act as if the button was clicked."""
    if event.keysym == "Return":
        button_click()
    elif event.char.isdigit():
        thousands_entry.focus()
 
 
def thousands_handler(event):
    """If the Enter key was pressed, act as if the button was clicked."""
    if event.keysym == "Return":
        button_click()
 
 
def button_click():
    """Check the user's answer against the correct answer."""
    if check_answer():
        game.score += 1
        your_score_label["text"] = f"スコア：{game.score}"
    else:
        game.lives -= 1
        hearts_label["text"] = game.remaining_hearts()
        Popup("違います！", f"正しい答え：{problem.answer}")
    if game.lives < 1:
        end_game()
    else:
        next_problem()
 
 
# Constants
FONT = "Consolas"
ENTRY_FONT = (FONT, 40, "normal")
BIG_SIZE = 48
 
# Creating the window
window = tkinter.Tk()
window.title("足し算 ゲーム")
window.minsize(width=500, height=260)
window.protocol("WM_DELETE_WINDOW", end_game)
validation = (window.register(entry_validation), "%P")
 
# Creating the variables that hold the entry field values
ones_value = tkinter.StringVar()
tens_value = tkinter.StringVar()
hundreds_value = tkinter.StringVar()
thousands_value = tkinter.StringVar()
 
# Creating the Game and MathProblem objects
problem = MathProblem()
game = Game()
 
# Creating window controls
num1_label = tkinter.Label(width=5, font=(FONT, BIG_SIZE, "normal"))
num2_label = tkinter.Label(width=5, font=(FONT, BIG_SIZE, "underline"))
hearts_label = tkinter.Label(text=game.remaining_hearts(), font=(FONT, 30, "normal"))
your_score_label = tkinter.Label(text=f"スコア：{game.score}", font=(FONT, 20, "normal"))
high_score_label = tkinter.Label(text=f"ハイスコア：{game.high_score}", font=(FONT, 20, "normal"))
 
ones_entry = tkinter.Entry(width=1, font=ENTRY_FONT, justify=tkinter.RIGHT, textvariable=ones_value, validate="key", validatecommand=validation)
tens_entry = tkinter.Entry(width=1, font=ENTRY_FONT, justify=tkinter.RIGHT, textvariable=tens_value, validate="key", validatecommand=validation)
hundreds_entry = tkinter.Entry(width=1, font=ENTRY_FONT, justify=tkinter.RIGHT, textvariable=hundreds_value, validate="key", validatecommand=validation)
thousands_entry = tkinter.Entry(width=1, font=ENTRY_FONT, justify=tkinter.RIGHT, textvariable=thousands_value, validate="key", validatecommand=validation)
 
answer_button = tkinter.Button(text="答えの確認", font=(FONT, 20, "normal"), command=button_click)
 
# Binding event handlers
ones_entry.bind("<Any-KeyPress>", ones_handler)
tens_entry.bind("<Any-KeyPress>", tens_handler)
hundreds_entry.bind("<Any-KeyPress>", hundreds_handler)
thousands_entry.bind("<Any-KeyPress>", thousands_handler)
 
# Placing window controls
num1_label.place(x=278, y=10)
num2_label.place(x=278, y=75)
hearts_label.place(x=10, y=10)
your_score_label.place(x=74, y=70)
high_score_label.place(x=25, y=105)
 
ones_entry.place(x=420, y=155)
tens_entry.place(x=385, y=155)
hundreds_entry.place(x=350, y=155)
thousands_entry.place(x=315, y=155)
 
answer_button.place(x=50, y=162)
 
# Generating the first problem (new problems are normally generated on button click)
next_problem()
 
window.mainloop()
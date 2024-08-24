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

# ---------------------------- SCREEN SETUP ------------------------------- # 
screen = Tk()
screen.minsize(width = 500, height = 500)
screen.config(padx = 120, pady = 120, bg = YELLOW)

# ---------------------------- TIMER RESET ------------------------------- # 
timer = Label(text = "TIMER",bg = YELLOW, fg = GREEN, font = (FONT_NAME, 30, "bold"))
timer.grid(row = 0, column = 1)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    count_down(5 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min_count_down = math.floor(count/60)
    sec_count_down = count%60
    if sec_count_down == 0:
        sec_count_down = "00"
    
    canvas.itemconfig(timer_record, text = f"{min_count_down}:{sec_count_down}" )
    if count > 0:
        screen.after(1000, count_down, count - 1)
# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato = PhotoImage(file = "pomodoro-start\\tomato.gif")
canvas.create_image(100, 112, image = tomato)
timer_record = canvas.create_text(100, 130, text = "00:00", font =(FONT_NAME, 35, "bold"),fill = "#FFFFFF")
canvas.grid(row = 1, column = 1)
 
start = Button(text = "Start", highlightthickness = 0, command = start_time)
reset = Button(text = "Reset", highlightthickness = 0)
start.grid(row = 2, column = 0)
reset.grid(row = 2, column = 2)

tick = Label(text = "✔",bg = YELLOW, fg = GREEN, font = (20))
tick.grid(row = 3, column = 1)

screen.mainloop()
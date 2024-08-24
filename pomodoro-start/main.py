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
rep = 0
activity = None

# ---------------------------- SCREEN SETUP ------------------------------- # 
screen = Tk()
screen.minsize(width = 500, height = 500)
screen.config(padx = 120, pady = 120, bg = YELLOW)
screen.title("Pomodoro")

# ---------------------------- TIMER RESET ------------------------------- # 
timer = Label(text = "TIMER",width = 11,bg = YELLOW, fg = GREEN, font = (FONT_NAME, 30, "bold"))
timer.grid(row = 0, column = 1)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global rep 
    rep += 1
    work_time = WORK_MIN 
    short_break = SHORT_BREAK_MIN 
    long_break = LONG_BREAK_MIN 
    
    if rep%8 == 0:
        count_down(long_break)
        timer.config(text = "Long Break", fg = RED)
        rep = 0
    elif rep%2 == 0:
        count_down(short_break)
        timer.config(text = "Short Break", fg = PINK)
    else:
        count_down(work_time)
        timer.config(text = "Work", fg = GREEN)

        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    start["state"] = "disabled"
    start["disabledforeground"] = start["foreground"]
    min_count_down = math.floor(count/60)
    sec_count_down = count%60
    if sec_count_down == 0:
        sec_count_down = "00"
    elif int(sec_count_down) < 10:
        sec_count_down = f"0{sec_count_down}"
    if min_count_down < 10:
        min_count_down = f"0{min_count_down}"

    
    canvas.itemconfig(timer_record, text = f"{min_count_down}:{sec_count_down}" )
    if count > 0:
        global activity
        activity = screen.after(1000, count_down, count - 1)
    else:
        start_time()
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
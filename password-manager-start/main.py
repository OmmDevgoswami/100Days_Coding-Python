from tkinter import *
from tkinter import font

PINK = "#e2979c"
RED = "#e7305b"
GRAY = "#eaeded"
YELLOW = "#f7f5dd"
VIOLET = "#6c3483"
 
# ---------------------------- SCREEN SETUP ------------------------------- # 
screen = Tk()
screen.minsize(width = 400, height = 500)
screen.config(padx = 120, pady = 35, bg=YELLOW)
screen.title("Password Manager")

font_path_1 = "password-manager-start\\Font\\Fjalla_One\\FjallaOne-Regular.ttf"
FONT_1 = font.Font(family="Fjalla One", size=14)
font_path_2 = "password-manager-start\\Font\\Hammersmith_One\\HammersmithOne-Regular.ttf"
FONT_2 = font.Font(family="Hammersmith One", size=14)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
canvas =  Canvas(width=300, height=200, highlightthickness=0, bg= YELLOW)
icon = PhotoImage(file="password-manager-start\\logo.png")
canvas.create_image(200, 100, image = icon)
canvas.grid(row=1, column=1)

website_label = Label(text="Website: ",font = FONT_1,bg = YELLOW, fg = PINK)
website_label.grid(row=2, column=0, sticky = "e")
website_entry = Entry(width = 35, font = FONT_2, bg = GRAY, fg = VIOLET)
website_entry.grid(row=2, column=1, columnspan=2, sticky = "w")

email_label = Label(text="Email: ",font = FONT_1, bg = YELLOW, fg = PINK)
email_label.grid(row=3, column=0, sticky = "e")
email_entry = Entry(width = 35, font = FONT_2, fg = VIOLET, bg = GRAY)
email_entry.grid(row=3, column=1, columnspan=2, sticky = "w")

user_label = Label(text="Username: ",font = FONT_1, bg = YELLOW, fg = PINK)
user_label.grid(row=4, column=0, sticky = "e")
user_entry = Entry(width = 35, font = FONT_2, bg = GRAY, fg = VIOLET)
user_entry.grid(row=4, column=1, columnspan=2, sticky = "w")

password_label = Label(text="Password: ",font = FONT_1, bg = YELLOW, fg = PINK)
password_label.grid(row=5, column=0,sticky = "e")
password_entry = Entry(width = 25, font = FONT_2, bg = GRAY, fg = VIOLET)
password_entry.grid(row=5, column=1,columnspan=2, sticky= "w")
pass_generator = Button(text = "Generate", font = FONT_2, highlightthickness = 0,bd = 0, bg = YELLOW, fg = RED,width = 10, relief=RAISED)
pass_generator.grid(row = 5, column = 2)

add_button = Button(text = "Record", font = FONT_2, highlightthickness = 0,bd = 0, bg = YELLOW, fg = RED, width = 40, relief=RAISED)
add_button.grid(row = 6, column = 1, columnspan=3)


screen.mainloop()
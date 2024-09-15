from tkinter import *
from tkinter import font
import pandas

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

# ---------------------------- SAVER-SCREEN SETUP ------------------------------- #
def confirm_page():
    saver = Toplevel(screen)
    saver.minsize(width=600, height=100)
    saver.config(padx=10, pady=10, bg=YELLOW)
    saver.title("Value Recorded Prompt")
    
    prompt = Label(saver, text="Information Recorded Successfully!!", font=FONT_1, bg=YELLOW, fg=PINK)
    prompt.pack(pady=10)

    def quit():
        saver.destroy()

    saver_button = Button(saver, text="Confirm", font=FONT_2, highlightthickness=0, bd=0, bg=YELLOW, fg=RED, width=10, relief=RAISED, command=quit)
    saver_button.pack(pady=10)
    
    print("Information Recorded Successfully!!!")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    
    with open("password-manager-start\\Details.txt", 'a') as file:
        file.write(f"\n{website} | {email} | {user} | {password}")
    
    Data = {
            "Website":[website],
            "Email":[email],
            "User":[user],
            "Password":[password]
        }
    new_data = pandas.DataFrame(Data)
    new_data.to_csv("password-manager-start\\Deatils.csv",mode='a', header=False, index=False)
    
    confirm_page()
    
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    user_entry.delete(0,END)
    password_entry.delete(0,END)  
      
    website_entry.focus()

    
# ---------------------------- UI SETUP ------------------------------- #
canvas =  Canvas(width=300, height=200, highlightthickness=0, bg= YELLOW)
icon = PhotoImage(file="password-manager-start\\logo.png")
canvas.create_image(200, 100, image = icon)
canvas.grid(row=1, column=1)

website_label = Label(text="Website: ",font = FONT_1,bg = YELLOW, fg = PINK)
website_label.grid(row=2, column=0, sticky = "e")
website_entry = Entry(width = 35, font = FONT_2, bg = GRAY, fg = VIOLET)
website_entry.focus()
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

add_button = Button(text = "Record", font = FONT_2, highlightthickness = 0,bd = 0, bg = YELLOW, fg = RED, width = 40, relief=RAISED, command = save)
add_button.grid(row = 6, column = 1, columnspan=3)

screen.mainloop()
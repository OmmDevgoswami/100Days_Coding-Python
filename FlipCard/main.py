import random
import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

def languageSelection():
    selector = Tk()
    selector.minsize(height=200, width=200)
    selector.title("Language Selection Region")
    selector.config(padx=10, pady=20, bg=BACKGROUND_COLOR)
    
    heading = Label(text="Select the Language You Wanna Practice Today !!", font=("Arial", 24, "bold"))
    heading.grid(row=0, column=1, pady=(0, 20))
    
    def quit():
        selector.destroy()
        selected_lang = langVal.get()
        getStarted(selected_lang)
    
    langVal = IntVar()
    Ja = Button(text="Japanese", command=lambda: langVal.set(1), highlightthickness=0, font=("Arial", 20))
    Ja.grid(row=1, column=0, pady=10)
    Fr = Button(text="French", command=lambda: langVal.set(2), highlightthickness=0, font=("Arial", 20))
    Fr.grid(row=1, column=1, pady=10)
    De = Button(text="German", command=lambda: langVal.set(3), highlightthickness=0, font=("Arial", 20))
    De.grid(row=1, column=2, pady=10)
    
    begin = Button(text="Start Learning !!", font=("Arial", 20, "italic"), highlightthickness=0, command=quit)
    begin.grid(row=2, column=1, pady=(10, 0))
    
    selector.grid_columnconfigure(0, weight=1)
    selector.grid_columnconfigure(1, weight=1)
    selector.grid_columnconfigure(2, weight=1)
    
    selector.mainloop()

def getStarted(choice):
    screen = Tk()
    screen.minsize(height=750, width=850)
    screen.title("Language Cards")
    screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    
    canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
    flipSide = PhotoImage(file="FlipCard\\images\\card_back.png")
    dashboard = PhotoImage(file="FlipCard\\images\\card_front.png")
    canvas_image = canvas.create_image(400, 270, image=dashboard)
    Language_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
    Words = canvas.create_text(400, 280, text="", font=("Arial", 50, "bold"))
    canvas.grid(row=1, column=0, columnspan=2)
    
    text_val = ""
    translation = ""
    learnt = {}

    def getrandom():
        nonlocal text_val, translation
        
        words = language.to_dict()
        size = len(language)
        
        if len(learnt) >= size:
            canvas.itemconfig(Language_title, text="Congratulations!", fill="black")
            canvas.itemconfig(Words, text="You’ve practiced all words!", fill="black")
            canvas.itemconfig(canvas_image, image=dashboard)
            correct.config(state=DISABLED)
            wrong.config(state=DISABLED)
            return
        
        while True:
            rand = random.randint(0, size - 1)
            text_val = words[lang][rand]
            translation = words["English"][rand]
            
            if text_val not in learnt:
                learnt[text_val] = translation 
                break  
            
        canvas.itemconfig(Language_title, text=lang, fill="black")
        canvas.itemconfig(Words, text=text_val, fill="black")
        canvas.itemconfig(canvas_image, image=dashboard)

    match(choice):
        case 1: 
            language = pandas.read_csv("FlipCard\\data\\Japanese-Eglish - Sheet1.csv")
            lang = "Japanese"
        case 2: 
            language = pandas.read_csv("FlipCard\\data\\french_words.csv")
            lang = "French"
        case 3: 
            language = pandas.read_csv("FlipCard\\data\\German-English - Sheet1.csv")
            lang = "German"
    
    getrandom()  

    correct_img = PhotoImage(file="FlipCard\\images\\right.png")
    wrong_img = PhotoImage(file="FlipCard\\images\\wrong.png")

    correct = Button(image=correct_img, highlightthickness=0, bd=0, command=getrandom)
    correct.grid(row=2, column=1)

    def flip():
        nonlocal text_val, translation
        canvas.itemconfig(Language_title, text="English", fill="white")
        canvas.itemconfig(canvas_image, image=flipSide)
        canvas.itemconfig(Words, text=translation, fill="white")
        screen.after(3000, flip_back)
    
    def flip_back():
        nonlocal text_val, translation
        canvas.itemconfig(Language_title, text=lang, fill="black")
        canvas.itemconfig(canvas_image, image=dashboard)
        canvas.itemconfig(Words, text=text_val, fill="black")

    wrong = Button(image=wrong_img, highlightthickness=0, bd=0, command=flip)
    wrong.grid(row=2, column=0)
    
    def auto_flip():
        flip()
        
    screen.after(3000, auto_flip)
    
    screen.mainloop()

languageSelection()

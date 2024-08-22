from tkinter import *

screen = Tk()
screen.title("Km to miles Converter")
screen.minsize(width = 300, height = 300)
screen.config(padx = 70, pady = 50)
Font = ("Helvetica", 20)

def km_to_miles():
    unit1_entry = Entry(width = 10, font = Font)
    unit1_entry.focus()
    unit1_entry.grid(row = 3, column = 2, padx = 10, pady = 10)
    print(unit1_entry.get())
    unit_1 = Label(text="Km", font = Font)
    unit_1.grid(row = 3, column = 3)

    text = Label(text = "is equal to:", font = Font)
    text.grid(row = 5, column = 1)
    unit2_value = Label(text = 0, font = Font)
    unit2_value.grid(row = 5, column = 2, padx = 10, pady = 10)
    unit_2 = Label(text="miles", font = Font)
    unit_2.grid(row = 5, column = 3)
    
    def convert():
        unit1_value = float(unit1_entry.get())
        converted_value = round(unit1_value*0.62137, 3)
        unit2_value.config(text = converted_value)
        
    button = Button(text = "Convert", command = convert)
    button.grid(row = 7, column = 2)

def miles_to_km():
    unit1_entry = Entry(width = 10, font = Font)
    unit1_entry.focus()
    unit1_entry.grid(row = 3, column = 2, padx = 10, pady = 10)
    print(unit1_entry.get())
    unit_1 = Label(text="miles", font = Font)
    unit_1.grid(row = 3, column = 3)

    text = Label(text = "is equal to:", font = Font)
    text.grid(row = 5, column = 1)
    unit2_value = Label(text = 0, font = Font)
    unit2_value.grid(row = 5, column = 2, padx = 10, pady = 10)
    unit_2 = Label(text="Km", font = Font)
    unit_2.grid(row = 5, column = 3)
    
    def convert():
        unit1_value = float(unit1_entry.get())
        converted_value = round(unit1_value*1.609344, 3)
        unit2_value.config(text = converted_value)
        
    button = Button(text = "Convert", command = convert)
    button.grid(row = 7, column = 2)

label = Label(text="Welcome to the Unit Conversion !!", font = Font)
label.grid(row = 1, column = 1)

def get_value():
    option = value_cap.get()
    for widget in screen.winfo_children():
        widget.destroy()
    if option == 1:
        km_to_miles()
    elif option == 2:
        miles_to_km()
        
value_cap = IntVar()
option_1 = Radiobutton(screen, text = "km_to_miles", value = 1, variable = value_cap)
option_2 = Radiobutton(screen, text = "miles_to_km", value = 2, variable = value_cap)
option_1.grid(row = 2, column = 1)
option_2.grid(row = 3, column = 1)

start = Button(screen, text = "Start", command = get_value)
start.grid(row = 5, column = 1)


screen.mainloop()
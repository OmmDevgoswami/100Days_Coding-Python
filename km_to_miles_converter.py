from tkinter import *

screen = Tk()
screen.title("Km to miles Converter")
screen.minsize(width = 300, height = 300)
screen.config(padx = 70, pady = 50)
Font = ("Helvetica", 20)

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



screen.mainloop()
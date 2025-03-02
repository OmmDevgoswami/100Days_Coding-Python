from tkinter import *
from tkinter import font
from tkcalendar import Calendar
import datetime
from PIL import Image, ImageTk
import random

#-------------------------------------- UI -----------------------------------------------#
GRAY = "#eaeded"
YELLOW = "#f7f5dd"
VIOLET = "#6c3483"
RED = "#e7305b"
PINK = "#e2979c"

screen = Tk()
screen.minsize(width=1000, height=600)
screen.title("Airbnb Dashboard")
screen.config(bg=YELLOW)

font_path = "Airbnb Scraping\\Resources\\Hammersmith_One\\HammersmithOne-Regular.ttf"
FONT = font.Font(family="Hammersmith One", size=14)

for i in range(10):  # Adjust according to the number of rows in your layout
    screen.grid_rowconfigure(i, minsize=60)  # Reduce row height globally
#---------------------------------- BACKGROUND -------------------------------------------#
randomImage = ["BG1.jpeg", "BG2.jpeg", "BG3.jpeg", "BG4.jpeg", "BG5.jpeg", "BG6.jpeg"]
randomChoice = random.choice(randomImage)

canvas = Canvas(screen, width=1000, height=600)
image_path = f"Airbnb Scraping\\Resources\\Images\\{randomChoice}"
jpg_image = Image.open(image_path) 
png_image = jpg_image.convert("RGBA") 
resized_image = png_image.resize((1000, 600))
bg_image = ImageTk.PhotoImage(resized_image)
canvas.grid(row=0, column=0, rowspan=10, columnspan=10) 
canvas.create_image(0, 0, image=bg_image, anchor="nw")

#--------------------------------- FUNCTIONALITY ------------------------------------------#
def get_booking_details():
    check_in_date = None
    check_out_date = None

    def calender(date_type):
        def get_date():
            global check_in_date, check_out_date  

            selected_date = cal.get_date()  
            date_obj = datetime.datetime.strptime(selected_date, "%Y-%m-%d") 
            formatted_date = date_obj.strftime("%m-%d")  

            if date_type == "check-in":
                check_in_date = formatted_date
                checkIn_label.config(text=f"Check-In: {check_in_date}")
            elif date_type == "check-out":
                if check_in_date and formatted_date < check_in_date:
                    check_out_date = check_in_date
                    checkOut_label.config(text=f"Check-Out: {check_out_date}")
                else:
                    check_out_date = formatted_date
                    checkOut_label.config(text=f"Check-Out: {check_out_date}")

            dateSaver.destroy() 

        def disable_past_dates(event):
            selected_date = datetime.datetime.strptime(cal.get_date(), "%Y-%m-%d").date()
            today = datetime.date.today()
            if selected_date < today:
                cal.selection_set(today) 

        dateSaver = Toplevel(screen)
        dateSaver.title("Select the Stay Duration")
        dateSaver.geometry("300x300")
        dateSaver.config(bg=YELLOW)

        today = datetime.date.today()

        cal = Calendar(
            dateSaver,
            selectmode="day",
            year=today.year,
            month=today.month,
            day=today.day,
            date_pattern="yyyy-mm-dd",
            mindate=today,
            background="white",     
            foreground="violet",     
            headersbackground="pink",  
            normalbackground="lightblue",  
            weekendbackground="lightcoral",  
            weekendforeground="black",   
            selectbackground="orange",   
        )
        cal.pack(pady=20)

        cal.bind("<<CalendarSelected>>", disable_past_dates)

        button = Button(dateSaver, text="Get Date", font=("Arial", 12), bg=YELLOW, fg=RED, width=10, relief=RAISED, command=get_date)
        button.pack(pady=10)

    location_label = Label(screen, text="LOCATION:", font=("Arial", 16, "bold"), bg=PINK)
    location_label.grid(row=5, column=1, sticky="e", padx=3)
    location_entry = Entry(screen, width=40, font=("Arial", 14), bg=GRAY, fg=VIOLET)
    location_entry.focus()
    location_entry.grid(row=5, column=2, sticky="w", padx=3)

    property_label = Label(screen, text="PROPERTY No(s):", font=("Arial", 16, "bold"), bg=PINK)
    property_label.grid(row=6, column=1, sticky="e", padx=3)
    property_entry = Entry(screen, width=20, font=("Arial", 14), bg=GRAY, fg=VIOLET)
    property_entry.grid(row=6, column=2, sticky="w", padx=3)

    checkIn_label = Label(screen, text="Check-In Date:", font=("Arial", 16, "bold"), bg=PINK)
    checkIn_label.grid(row=7, column=1, sticky="e", padx=5, pady=5)
    checkIn_button = Button(screen, text="Select", font=FONT, bg=YELLOW, fg=RED, width=10, relief=RAISED, command=lambda: calender("check-in"))
    checkIn_button.grid(row=7, column=2, sticky="w", padx=5, pady=5)

    checkOut_label = Label(screen, text="Check-Out Date:", font=("Arial", 16, "bold"), bg=PINK) 
    checkOut_label.grid(row=7, column=2, sticky="e", padx=5, pady=5)
    checkOut_button = Button(screen, text="Select", font=FONT, bg=YELLOW, fg=RED, width=10, relief=RAISED, command=lambda: calender("check-out"))
    checkOut_button.grid(row=7, column=3, sticky="w", padx=5, pady=5)

    def submit():
            global check_in_date, check_out_date
            userLocation = location_entry.get()
            propertyNo = property_entry.get()
            details = [userLocation, propertyNo, check_in_date, check_out_date]
            checkIn = check_in_date
            checkOut = check_out_date
            print(userLocation)
            print(propertyNo)
            print(checkIn)
            print(checkOut)
            screen.quit()  
            screen.destroy()
            screen.result = details  
            
    submit_button = Button(screen, text="Submit", font=FONT, bg=VIOLET, fg="white", width=15, relief=RAISED, command = submit)
    submit_button.grid(row=8, column=2, pady=10)

    screen.mainloop()
    return screen.result

get_booking_details()
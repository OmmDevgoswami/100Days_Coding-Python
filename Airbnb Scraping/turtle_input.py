from tkinter import *
from PIL import Image, ImageTk

# Initialize screen
screen = Tk()
screen.minsize(width=400, height=500)

# Load image (use PIL for JPG or PNG images)
image_path = "background.png"  # Change to your image path
bg_image = PhotoImage(file=image_path)  # Use ImageTk.PhotoImage if JPG

# Create Canvas
canvas = Canvas(screen, width=400, height=500)
canvas.grid(row=0, column=0, rowspan=5, columnspan=5)  # Span entire grid

# Place image on Canvas
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Add widgets on top of the canvas
label = Label(screen, text="Welcome!", font=("Arial", 16, "bold"), bg="white")
label.grid(row=1, column=2)  # Placing it on top of the background

button = Button(screen, text="Click Me", command=lambda: print("Clicked!"))
button.grid(row=2, column=2)

# Run main loop
screen.mainloop()

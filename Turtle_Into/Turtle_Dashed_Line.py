import turtle

turt = turtle.Turtle()
screen = turtle.Screen()
screen.title("Dashed Line Project")
turt.penup()
turt.goto(-200,0)
turt.pendown()

for _ in range (20):
    if (_ % 2 == 0):
        turt.color("orange")
    else:
        turt.color("blue")
    turt.forward(10)
    turt.penup()
    turt.forward(10)
    turt.pendown()
    
print ("Dash Line Drawing Completed !11")


turtle.done()
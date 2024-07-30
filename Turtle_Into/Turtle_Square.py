import turtle 


turt = turtle.Turtle()
bg = turtle.Screen()
bg.title("Square !!")
turt.shape("square")
turt.color("orange")
turt.fillcolor("pink")

turt.begin_fill() 
for i in range(0,4):    
    turt.forward(100)
    turt.right(90)
turt.end_fill()

print ("Drawing Square Completed !!")


turtle.done()


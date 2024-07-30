import turtle
import random

color_list = ["navajo white", "violet", "spring green", "cyan" , "yellow", "light steel blue", "lime", "dark violet", "wheat", "crimson", "indigo"]
shapes = ["Triangle", "Square", "Pentagon", "Hexagon", "Heptagon", "Octagon", "Nonagon", "Decagon"]


turt = turtle.Turtle()
screen = turtle.Screen()
screen.title("Different Shapes")
turt.penup()
turt.goto(-40,140)
turt.pendown()

for sides in range (3,11):
    turt.color(random.choice(color_list))
    angel = 360/sides
    for _ in range(sides):
        turt.forward(100)
        turt.right(angel)
    print (f"Shape : {shapes[sides-3]} printed")    
        
    
        
     
turtle.done()        
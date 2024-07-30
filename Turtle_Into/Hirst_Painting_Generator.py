# import colorgram
# color_extraction = colorgram.extract('paint.jpeg', 30)
""" cologram module is used to extract colors from a particular image and present them as a list of tuples. """

import turtle, random

def turtleMove(x, y):
    turt.penup()
    turt.goto(x, y)
    turt.pendown()


turtle.colormode(255)
color_list = [ (238, 248, 243), (251, 242, 246), (226, 237, 246), (30, 106, 145), (229, 153, 80), (15, 169, 207), (148, 79, 30), (6, 57, 97), (31, 134, 77), 
              (214, 133, 162), (138, 32, 51), (205, 156, 22), (118, 172, 194), (213, 93, 124), (235, 211, 85), (6, 103, 66), (145, 185, 167), (216, 209, 11), 
              (3, 69, 136), (15, 49, 43), (76, 83, 23), (243, 168, 151), (134, 59, 83), (53, 60, 15), (223, 170, 191), (230, 100, 40), (1, 90, 120), (71, 157, 105), (164, 29, 25)]

turt = turtle.Turtle()
screen = turtle.Screen()
screen.title("Hirst_Paint_Generator")
turt.speed(6)
turt.hideturtle()
x = -230
y = -220
turtleMove (x , y)

for _ in range(10):
    for dots in range(10):
        turt.dot(20, random.choice(color_list))
        turt.penup()
        turt.forward(50)
        turt.pendown() 
    y += 50    
    turtleMove(x, y)
    
    
turtle.done()    
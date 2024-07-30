import turtle
import random


def on_click(x, y):
    """ Used to move the turtle to the desired location. """
    turt.penup()
    turt.goto(x, y)
    turt.pendown()


def ifLost():
    """ When then the turtle goes out of the screen visibility, it can be used to call it back on to the screen. """
    screen.onclick(on_click)


color_list = ["navajo white", "violet", "spring green", "cyan" , "yellow", "light steel blue", "lime", "dark violet", "wheat", "crimson", "indigo", "chocolate", "navy"]
direction = [0, 90, 180, 270]

turt = turtle.Turtle()
screen = turtle.Screen()
screen.title("Different Shapes")
turt.pensize(7)

while True:
    turt.speed("fastest")
    turt.color(random.choice(color_list))
    turt.forward(40)
    turt.setheading(random.choice(direction))
    ifLost()   
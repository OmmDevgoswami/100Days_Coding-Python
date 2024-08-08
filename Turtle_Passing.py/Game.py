import turtle
import time
from Turtle_Boiii import Player

screen = turtle.Screen()
screen.title("Turtle !!!! Pass The Road Safely!!")
screen.setup(width = 600, height = 600)
screen.tracer(0)

turtle_boi = Player()

screen.listen()
screen.onkeypress(fun= turtle_boi.move_Forward, key ="Up")
screen.onkeypress(fun = turtle_boi.move_Forward, key = "w")

while True:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
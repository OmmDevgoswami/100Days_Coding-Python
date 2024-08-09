import turtle
import time
from Turtle_Boiii import Player
import Car
import level

screen = turtle.Screen()
screen.title("Turtle !!!! Pass The Road Safely!!")
screen.setup(width = 800, height = 600)
screen.tracer(0)

turtle_boi = Player()
game_level = level.Level()
cars = Car.Car_Object()

screen.listen()
screen.onkeypress(fun= turtle_boi.move_Forward, key ="Up")
screen.onkeypress(fun = turtle_boi.move_Forward, key = "w")

flag = True
while flag:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    
    if turtle_boi.ycor() > screen.window_height()/2 -20:
        turtle_boi.road_crossed()
        game_level.level_up()
    
    for car in cars.all_car:  
        if car.distance(turtle_boi) < 20:
            flag = False
       
screen.exitonclick()
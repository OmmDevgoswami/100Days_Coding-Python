import turtle
import time
import snake

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

new_snake = snake.Snake()


flag = True
while flag:
    screen.update()
    time.sleep(0.1)
    new_snake.move()
       
screen.exitonclick()
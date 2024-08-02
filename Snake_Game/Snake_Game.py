import turtle
import time
import snake

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

new_snake = snake.Snake()

screen.listen()
#Keyboard Events
screen.onkeypress(new_snake.up, "Up")
screen.onkeypress(new_snake.up, "w")

screen.onkeypress(new_snake.down, "Down")
screen.onkeypress(new_snake.down, "s")

screen.onkeypress(new_snake.left, "Left")
screen.onkeypress(new_snake.left, "a")

screen.onkeypress(new_snake.right, "Right")
screen.onkeypress(new_snake.right, "d")


flag = True
while flag:
    screen.update()
    time.sleep(0.1)
    new_snake.move()
       
screen.exitonclick()
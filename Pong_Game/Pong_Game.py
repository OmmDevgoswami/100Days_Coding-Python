import turtle
import paddle

screen = turtle.Screen()
screen.setup(width = 800, height = 600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

right_paddle = paddle.Paddle((350, 0))
left_paddle = paddle.Paddle((-350, 0))

screen.listen()
screen.onkey(fun = right_paddle.go_up,key = "Up")
screen.onkey(fun = right_paddle.go_down,key = "Down")
screen.onkey(fun = left_paddle.go_up,key = "w")
screen.onkey(fun = left_paddle.go_down,key = "s")

flag = True
while flag:
    screen.update()

screen.exitonclick()
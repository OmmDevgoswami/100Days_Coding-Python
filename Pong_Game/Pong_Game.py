import turtle
import time
import paddle
import ball
import score
import boarder

turt = turtle.Turtle()
turt.hideturtle()
turt.color("white")
screen = turtle.Screen()
screen.setup(width = 800, height = 600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

right_paddle = paddle.Paddle((screen.window_width()/2 - 50, 0))
left_paddle = paddle.Paddle((-screen.window_width()/2 + 50, 0))
game_ball = ball.Ball()
game_resources = boarder.Baorder()
right_score =  score.Score(30, screen.window_height()/2 - 50)
left_score = score.Score(-45, screen.window_height()/2 - 50)

screen.listen()
screen.onkeypress(fun = right_paddle.go_up,key = "Up")
screen.onkeypress(fun = right_paddle.go_down,key = "Down")
screen.onkeypress(fun = left_paddle.go_up,key = "w")
screen.onkeypress(fun = left_paddle.go_down,key = "s")

flag = True
speed = 0.1
while flag:
    time.sleep(speed)
    screen.update()
    game_ball.move()
    if abs(game_ball.ycor()) > screen.window_height()/2 - 20:
        game_ball.bounce()
    if abs(game_ball.xcor()) > screen.window_width()/2 - 70 and (game_ball.distance(right_paddle) < 50 or game_ball.distance(left_paddle) < 50):
        game_ball.rebound()
        speed -= 0.01
        
    if game_ball.xcor() > screen.window_width()/2 - 20:
        game_ball.home()
        speed = 0.1
        left_score.increase_score()
        
    if game_ball.xcor() < -screen.window_width()/2 - 20:
        game_ball.home()
        speed = 0.1
        right_score.increase_score()
    
    if left_score.game_score == 21:
        turt.write("Left House is the Winner !!")
        flag = False  
    elif right_score.game_score == 21:
        turt.write("Right House is the Winner !!")  
        flag = False
    
        
screen.exitonclick()
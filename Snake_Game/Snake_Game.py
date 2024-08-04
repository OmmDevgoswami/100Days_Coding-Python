import turtle
import time
import snake
import food
import scoreboard

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.setup(740, 740)

new_snake = snake.Snake()
new_food = food.Food()
score = scoreboard.Scoreboard()

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
    if new_snake.head.distance(new_food) < 15:
        new_food.refreshFood()
        score.increaseScore()
        new_snake.sizeIncrease()
    
    #Die on Touching The Wall  
    if abs(new_snake.head.xcor()) > 360 or abs(new_snake.head.ycor()) > 360:
        score.game_over()
        flag = False
        
    #Pass Through The Wall    
    # if new_snake.head.xcor() > 350 or new_snake.head.xcor() < -350:
    #     new_snake.head.setx(new_snake.head.xcor() * -1)
    # if new_snake.head.ycor() > 350 or new_snake.head.ycor() < -350:
    #     new_snake.head.sety(new_snake.head.ycor() * -1)
    
    for _ in new_snake.snake:
        if _ == new_snake.head:
            pass
        elif (new_snake.head.distance(_) < 10):
            score.game_over()
            flag = False
       
screen.exitonclick()
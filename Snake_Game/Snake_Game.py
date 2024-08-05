import turtle
import time
import snake
import food
import scoreboard

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(740, 740)

def level_input(prompt_title:str , prompt_message:str):
    """
    Level Choice.
    """
    user_input = turtle.textinput(prompt_title, prompt_message)
    while True:
        if user_input is None or user_input.strip() == "":
            user_input = turtle.textinput(prompt_title, prompt_message)
        else:
            return user_input

def Game(level:str):
    """
    Main Game Program
    """
    screen.tracer(0)

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

    #Game Loop
    flag = True
    while flag:
        screen.update()
        time.sleep(0.1)
        new_snake.move()
        if new_snake.head.distance(new_food) < 15:
            new_food.refreshFood()
            score.increaseScore()
            new_snake.sizeIncrease()
        
        if level == "easy":
        #Pass Through The Wall    
            if abs(new_snake.head.xcor()) > (screen.window_width()/2 - 20):
                new_snake.head.setx(new_snake.head.xcor() * -1)
            if abs(new_snake.head.ycor()) > (screen.window_height()/2 - 20):
                new_snake.head.sety(new_snake.head.ycor() * -1)
        elif level == "hard":        
        #Die on Touching The Wall
            boarder = turtle.Turtle()
            boarder.hideturtle()
            boarder.penup()
            boarder.goto(x = -screen.window_width()/2 + 7 , y = screen.window_height()/2 - 7)
            boarder.pendown()
            boarder.color("white")
            for _ in range(4):
                boarder.forward(screen.window_width() - 25)
                boarder.right(90)
            
            if abs(new_snake.head.xcor()) > (screen.window_width()/2 - 9) or abs(new_snake.head.ycor()) > (screen.window_height()/2 - 9):
                score.game_over()
                flag = False
        
        #Die if Touch Eatself        
        for _ in new_snake.snake:
            if _ == new_snake.head:
                pass
            elif (new_snake.head.distance(_) < 10):
                score.game_over()
                flag = False

level = level_input("Difficulty level","Choose Game Difficulty\n1.Easy\n2.Hard").lower()
Game(level)

       
turtle.done()
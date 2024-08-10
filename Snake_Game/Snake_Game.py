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


def highScore_update(level, current_score):
    """
    Function to Read and Update the New HighScore as per the games
    """
    with open(f"Snake_Game\\{level}HighScore.txt", mode = "r+") as file:
        high_score = file.read()
        if int(high_score) < current_score:           
            with open(f"Snake_Game\\{level}HighScore.txt", mode = "w") as file:
                    file.write(str(current_score))


def second_chance(level:str):    
    """
    Function to Restart ot End the Game
    """    
    restart_n_exit = turtle.textinput("Restart or Exit?", "Press 'r' to restart and 'e' to exit.").lower()
    if restart_n_exit == "r":
        screen.clearscreen()
        Game(level)
    elif restart_n_exit == "e":
        screen.bye()
       

def Game(level:str):
    """
    Main Game Program
    """
    screen.bgcolor("black")
    screen.tracer(0)

    new_snake = snake.Snake()
    new_food = food.Food()
    game_score = scoreboard.Scoreboard(level)
    current_score = 0

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
            game_score.increaseScore()
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
                game_score.game_over()
                flag = False
                current_score = game_score.score
        
        #Die if Touch Eatself        
        for _ in new_snake.snake:
            if _ == new_snake.head:
                pass
            elif (new_snake.head.distance(_) < 10):
                game_score.game_over()
                flag = False
                current_score = game_score.score
                
    #To Read and Update the New HighScore as per the games
    highScore_update(level, current_score)
                    
    #To call the second_chance function after 5secs
    screen.ontimer(lambda : second_chance(level), 5000)
            
       
level = level_input("Difficulty level","Choose Game Difficulty\n1.Easy\n2.Hard").lower()
Game(level)

       
turtle.done()
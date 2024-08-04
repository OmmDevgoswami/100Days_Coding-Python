import turtle
MOVE_DIRECTION = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """ 
    Creates a Snake Object
    """
    def __init__(self):
        self.snake = []
        self.create_Snake()
        self.head = self.snake[0]
        self.tail = self.snake[len(self.snake) -1]

    def create_Snake(self):
        """
        Creation of Snake using Turtle Module
        """
        for _ in range(3):
            snake_body = turtle.Turtle(shape = "square")
            snake_body.color("white")
            snake_body.penup()
            snake_body.goto(y = 0, x =( _*-20))
            self.snake.append(snake_body)
            
    
    def move(self):    
        """
        Used to Move the all the body segments of the snake together.
        """
        for seg_num in range(len(self.snake) - 1, 0, -1):
                snake_position = self.snake[seg_num - 1].position()
                self.snake[seg_num].goto(snake_position)   
        snake_position = self.snake[0].position()
        self.snake[1].goto(snake_position)
            
        self.snake[0].forward(MOVE_DIRECTION)
    
    def up(self):
        """ 
        First part of the Code Checks for direction change, 
        While seconf part check for invlaid move of self collision.
        """
        if self.head.heading() != DOWN and self.snake[0].ycor() != self.snake[1].ycor() - 20:
            self.head.setheading(UP)
 
    def down(self):
        """ 
        First part of the Code Checks for direction change, 
        While seconf part check for invlaid move of self collision.
        """
        if self.head.heading() != UP and self.snake[0].ycor() != self.snake[1].ycor() + 20:
            self.head.setheading(DOWN)
 
    def right(self):
        """
        First part of the Code Checks for direction change, 
        While seconf part check for invlaid move of self collision.
        """    
        if self.head.heading() != LEFT and self.snake[0].xcor() != self.snake[1].xcor() - 20:
            self.head.setheading(RIGHT)
 
    def left(self):
        """ 
        First part of the Code Checks for direction change, 
        While seconf part check for invlaid move of self collision.
        """
        if self.head.heading() != RIGHT and self.snake[0].xcor() != self.snake[1].xcor() + 20:
            self.head.setheading(LEFT)      

    def sizeIncrease(self):
        snake_body = turtle.Turtle(shape = "square")
        snake_body.color("white")
        snake_body.penup()
        head_position = self.tail.position()
        snake_body.goto(head_position)
        self.snake.insert(len(self.snake)-1, snake_body)
        self.move()

import turtle
MOVE_DIRECTION = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
INITIAL_IMAGE = ['Snake_Game\\Image_Resources\\head_right.gif', 'Snake_Game\\Image_Resources\\body_w_e.gif', 'Snake_Game\\Image_Resources\\tail_right.gif']
W_E_ORIENTATION = 'Snake_Game\\Image_Resources\\body_w_e.gif'
N_S_ORIENTATION = 'Snake_Game\\Image_Resources\\body_n_s.gif'
TAIL = ['Snake_Game\\Image_Resources\\tail_right.gif', 'Snake_Game\\Image_Resources\\tail_down.gif', 'Snake_Game\\Image_Resources\\tail_left.gif', 'Snake_Game\\Image_Resources\\tail_up.gif']
HEAD = ['Snake_Game\\Image_Resources\\head_right.gif', 'Snake_Game\\Image_Resources\\head_down.gif', 'Snake_Game\\Image_Resources\\head_left.gif', 'Snake_Game\\Image_Resources\\head_up.gif']

class Snake:
    """ 
    Creates a Snake Object
    """
    def __init__(self):
        self.snake = []
        self.body = []
        self.create_Snake()
        self.head = self.snake[0]
        self.tail = self.snake[len(self.snake) -1]
        

    def create_Snake(self):
        """
        Creation of Snake using Turtle Module
        """
        shape = turtle.Screen()
        for _ in range(3):
            shape.addshape(INITIAL_IMAGE[_])
        shape.addshape(W_E_ORIENTATION)
        shape.addshape(N_S_ORIENTATION)
        for _ in range(4):
            shape.addshape(TAIL[_])
            shape.addshape(HEAD[_])
        
        for _ in range(3):
            snake_body = turtle.Turtle()
            if _ == 1:
                snake_body.shape(INITIAL_IMAGE[_])
                self.body.append(snake_body)
                self.snake.append(snake_body)
            else:
                snake_body.shape(INITIAL_IMAGE[_])
                self.snake.append(snake_body)
            snake_body.penup()
            snake_body.goto(y = 0, x =( _*-20))


    def move(self):    
        """
        Used to Move the all the body segments of the snake together.
        """
        for seg_num in range(len(self.snake) - 1, 0, -1):
            if seg_num == 1:
                for _ in range(len(self.body)):
                    body_position = self.body[_].position()
                    self.snake[seg_num].goto(body_position)
            else:
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
            self.head.shape(HEAD[3])
            self.head.setheading(UP)
            self.tail.shape(TAIL[3])
            # self.tail.setheading(UP)
            for _ in range(len(self.body)):
                self.body[_].shape(N_S_ORIENTATION)
            
 
    def down(self):
        """ 
        First part of the Code Checks for direction change, 
        While seconf part check for invlaid move of self collision.
        """
        if self.head.heading() != UP and self.snake[0].ycor() != self.snake[1].ycor() + 20:
            self.head.shape(HEAD[1])
            self.head.setheading(DOWN)
            self.tail.shape(TAIL[1])
            # self.tail.setheading(DOWN)
            for _ in range(len(self.body)):
                self.body[_].shape(N_S_ORIENTATION)
            
 
    def right(self):
        """
        First part of the Code Checks for direction change, 
        While seconf part check for invlaid move of self collision.
        """    
        if self.head.heading() != LEFT and self.snake[0].xcor() != self.snake[1].xcor() - 20:
            self.head.shape(HEAD[0])
            self.head.setheading(RIGHT)
            self.tail.shape(TAIL[0])
            # self.tail.setheading(RIGHT)
            for _ in range(len(self.body)):
                self.body[_].shape(W_E_ORIENTATION)
            
 
    def left(self):
        """ 
        First part of the Code Checks for direction change, 
        While seconf part check for invlaid move of self collision.
        """
        if self.head.heading() != RIGHT and self.snake[0].xcor() != self.snake[1].xcor() + 20:
            self.head.shape(HEAD[0])
            self.head.setheading(LEFT)
            self.tail.shape(TAIL[2]) 
            # self.tail.setheading(LEFT)
            for _ in range(len(self.body)):
                self.body[_].shape(W_E_ORIENTATION)     

    def update_segment_directions(self, direction):
        """
        Update the heading of each segment based on the segment in front of it.
        """
        if direction == UP:
            for _ in range(len(self.body)):
                    self.body[_].shape(N_S_ORIENTATION)
        elif direction == RIGHT:
            for _ in range(len(self.body)):
                self.body[_].shape(W_E_ORIENTATION) 
    

    def sizeIncrease(self):
        """
        Increase the Size of the Turtle Created.
        """
        snake_body = turtle.Turtle()
        snake_body.shape(INITIAL_IMAGE[1])
        snake_body.penup()
        head_position = self.head.position()
        head_direction = self.head.heading()
        snake_body.goto(head_position)
        self.body.append(snake_body)
        self.snake.insert(len(self.snake)-1, snake_body)
        if head_direction == UP or head_direction == DOWN:
            self.update_segment_directions(UP)
        elif head_direction == RIGHT or head_direction == LEFT:
            self.update_segment_directions(RIGHT) 
        self.move()
        
        
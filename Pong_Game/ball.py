import turtle

MOVE_X = 10
MOVE_Y = 10

class Ball(turtle.Turtle):
    """
    A Ball object is being created using Turtle Module.
    """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        
       
       
    def move(self):
        """
        To Move the ball across the screen.
        """
        self.x_position = self.xcor() + MOVE_X 
        self.y_position = self.ycor() + MOVE_Y 
        self.goto(x = self.x_position, y = self.y_position)
        

    def bounce(self):
        """
        To Change the Direction of the Ball After it bounces of the Upper and Lower Wall.
        """
        global MOVE_Y
        MOVE_Y *= -1
        
    def rebound(self):
        """
        To Change the Direction of the Ball After it bounces of the Paddle.
        """
        global MOVE_X
        MOVE_X *= -1
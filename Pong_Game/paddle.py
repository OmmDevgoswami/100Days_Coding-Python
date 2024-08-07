import turtle

class Paddle(turtle.Turtle):
    """
    A class to represent a paddle in the game.
    """
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid = 5, stretch_len= 1)
        self.penup()
        self.goto(position)   
        
    def go_up(self):
        """
        Function to move the paddle in upward direction.
        """
        if self.ycor() < 250:
            self.y_position = self.ycor() + 20
            self.goto(x = self.xcor(), y = self.y_position)
        else:
            self.goto(x = self.xcor(), y = self.y_position)
    
    def go_down(self):
        """
        Function to move the paddle in downward direction.
        """
        if self.ycor() > -250:
            self.y_position = self.ycor() - 20
            self.goto(x = self.xcor(), y = self.y_position)
        else:
            self.goto(x = self.xcor(), y = self.y_position)
    
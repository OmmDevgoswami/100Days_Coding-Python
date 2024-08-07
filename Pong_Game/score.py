import turtle

FONT = ("Courier", 24, "normal")

class Score(turtle.Turtle):
    """
    To create a score class using turtle inheritance
    """
    def __init__(self, x_position, y_position):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.game_score = 0 
        self.penup()
        self.goto(x = x_position, y = y_position)
        self.pendown()
        self.score()
    
    def score (self):
        """
        Function to display the score of each player.
        """
        self.write(self.game_score, font = FONT)
    
    
    def increase_score(self):
        """
        Function to incrase the score of each player by 1 point when the opponent misses the ball.
        """
        self.game_score += 1 
        self.clear()
        self.score()        
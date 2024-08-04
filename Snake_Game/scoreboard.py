import turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(turtle.Turtle):
    """
    Creation of Score by inheritance of Turtle Module
    """
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.screen = turtle.Screen()
        self.color("gold")
        self.goto(x = 0,  y = int(self.screen.window_height()/2 - 40))
        self.pendown()
        self.write (f"Score: {self.score}" ,align = ALIGNMENT ,font = FONT)
        self.hideturtle()
        
    def updateScore(self):
        """
        Updating the Score
        """
        self.write (f"Score: {self.score}" ,align = ALIGNMENT ,font = FONT)
        
    def increaseScore(self):
        """
        Increasing th Score by 1
        """
        self.score += 1
        self.clear()
        self.updateScore()
        
    def game_over(self):
        """
        Game Over Function !!!
        """
        self.home()
        self.write(" Game Over!! ", align = ALIGNMENT, font = FONT)
    
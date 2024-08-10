import turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(turtle.Turtle):
    """
    Creation of Score by inheritance of Turtle Module
    """
    def __init__(self, level):
        super().__init__()
        self.score = 0
        with open(f"Snake_Game\\{level}HighScore.txt", mode = "r") as file:
                    self.new_score = file.read()
                    if self.new_score:
                        self.highscore = int(self.new_score)
                    else:
                        self.highscore = 0
        # self.restart(new_Score)
        self.penup()
        self.screen = turtle.Screen()
        self.color("gold")
        self.goto(x = 0,  y = int(self.screen.window_height()/2 - 40))
        self.pendown()
        self.updateScore()
        self.hideturtle()
        
    def updateScore(self):
        """
        Updating the Score
        """
        self.write (f"Score: {self.score}  HighScore: {self.highscore}" ,align = ALIGNMENT ,font = FONT)
        
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
    
    def restart(self, new_score):
        self.penup()
        if new_score > self.highscore:
            self.highscore = new_score
        self.score = 0
        
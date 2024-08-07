import turtle

FONT = ("Courier", 24, "normal")

class Score(turtle.Turtle):
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
        self.write(self.game_score, font = FONT)
    
    
    def increase_score(self):
        self.game_score += 1 
        self.clear()
        self.score()        
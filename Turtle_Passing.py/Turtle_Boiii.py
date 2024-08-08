import turtle
import level

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.screen = turtle.Screen()
        self.penup()
        self.left(90)
        self.goto(x = 0, y = -self.screen.window_height()/2 + 20)    
        
        
    def move_Forward(self):
        self.forward(10)
    
        
    def road_crossed(self):
        self.goto(x = 0, y = -self.screen.window_height()/2 + 20)
        self.game_level = level.Level()
        y_position = self.ycor()
        if y_position == (self.screen.window_height()/2 - 20):
            self.game_level.level_up()
    

import turtle

class Level(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.current_level()
        
    def current_level(self):
        self.screen = turtle.Screen()
        self.goto (x = -self.screen.window_width()/2 + 30, y = self.screen.window_height()/2 - 30)
        self.write (f"Level : {self.level}")
    
        
    def level_up(self):
        self.level += 1
        self.clear()
        self.current_level()
import turtle
import random

class Food(turtle.Turtle):
    """
    Creation of Food by inheritance of Turtle Module
    """
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('orange') 
        self.shapesize(stretch_wid = 0.5, stretch_len = 0.5) 
        self.penup()
        self.speed("fastest")
        self.refreshFood()
        
        
    def refreshFood(self):
        """
        Change the position of the food when Snake eats the previous one.
        """
        self.screen = turtle.Screen()
        self.x_position = random.randrange(-int(self.screen.window_width() / 2 - 20), int(self.screen.window_width() / 2 - 20))
        self.y_position = random.randrange(-int(self.screen.window_height() / 2 - 20), int(self.screen.window_height() / 2 - 20))
        self.goto(x = self.x_position ,y = self.y_position) 
        
        
import turtle

class Baorder(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.x = self.screen.window_width()
        self.y = self.screen.window_height()
        self.hideturtle()
        self.draw_boarder()
        
        
    def draw_boarder(self):
        self.screen = turtle.Screen()
        self.penup()
        self.goto(x = -(self.x)/2 - 10 , y = (self.y)/2 - 2)
        self.pendown()
        self.forward(self.x)
        self.penup()
        self.goto(x = -(self.x)/2 - 10 , y = -(self.y)/2 + 10)
        self.pendown()
        self.forward(self.x)
        self.penup()
        self.goto(x = 0, y = (self.y)/2 - 2)
        self.pendown()
        self.right(90)
        for _ in range(int((self.y)/7.5)):
            if _%2 == 0:
                self.forward(10)
            else:
                self.penup()
                self.forward(5)
                self.pendown()    
import turtle

class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid = 5, stretch_len= 1)
        self.penup()
        self.goto(position)   
        
    def go_up(self):
        if self.ycor() < 250:
            self.y_position = self.ycor() + 20
            self.goto(x = self.xcor(), y = self.y_position)
        else:
            self.goto(x = self.xcor(), y = self.y_position)
    
    def go_down(self):
        if self.ycor() > -250:
            self.y_position = self.ycor() - 20
            self.goto(x = self.xcor(), y = self.y_position)
        else:
            self.goto(x = self.xcor(), y = self.y_position)
    
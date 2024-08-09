import turtle
import random
COLOR = ["Red", "Orange", "Yellow", "Blue", "Green", "Violet"]

class Car_Object():
    def __init__(self):
        self.screen = turtle.Screen()
        self.all_car = []
        self.create_car()
        self.auto_move()
               
            
    def create_car(self):
        self.car_timing = random.randint(1,6)
        if self.car_timing == 1:
            car = turtle.Turtle(shape = "square")
            car.right(180)
            car.penup()
            car.shapesize(stretch_wid = 1,stretch_len = 2)
            car.color(random.choice(COLOR))
            self.starting_position(car)
            self.all_car.append(car)
        else:
            turtle.hideturtle()
        
    
    
    def starting_position(self, car):
        y_pos = self.screen.window_height()/2 - 60
        y_neg = -self.screen.window_height()/2 + 60
        y_position = random.randrange(y_neg, y_pos+1, 20)
        car.goto (x = self.screen.window_width()/2, y = y_position)
        
    
    def auto_move(self):
        for car in self.all_car:
            car.forward(10)
            if car.xcor() < -self.screen.window_width() / 2:  
                car.goto(self.screen.window_width() / 2, car.ycor())
        self.screen.ontimer(self.auto_move, 50)   

import turtle
class Snake:
    def __init__(self):
        self.snake = []
        self.create_Snake()

    def create_Snake(self):
        for _ in range(3):
            snake_body = turtle.Turtle(shape = "square")
            snake_body.color("white")
            snake_body.penup()
            snake_body.goto(y = 0, x =( _*-20))
            self.snake.append(snake_body)
    
    def move(self):    
        for seg_num in range(len(self.snake) - 1, 0, -1):
                snake_position = self.snake[seg_num - 1].position()
                self.snake[seg_num].goto(snake_position)   
        snake_position = self.snake[0].position()
        self.snake[1].goto(snake_position)
            
        self.snake[0].forward(20)
        self.snake[0].left(90)    
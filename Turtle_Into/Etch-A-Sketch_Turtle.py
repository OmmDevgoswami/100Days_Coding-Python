import turtle

turt = turtle.Turtle()
screen = turtle.Screen()
screen.title("Etch-A-Sketch")
turt.speed("fastest")

def moveForward():
    turt.forward(10)
    
def moveBackward():
    turt.backward(10)
    
def rotateLeft():
    turt.left(10)
    
def rotateRight():
    turt.right(10)
    
def clearScreen():
    # turt.speed("fastest")
    # turt.home()
    # turt.clear()
    # turt.speed("normal")
    turt.reset()
    
    
screen.onkey(fun = moveForward, key = "w")
screen.onkey(fun = moveForward, key = "Up")

screen.onkey(fun = moveBackward, key = "s")
screen.onkey(fun = moveBackward, key = "Down")

screen.onkey(fun = rotateLeft, key = "a")
screen.onkey(fun = rotateLeft, key = "Left")

screen.onkey(fun = rotateRight, key = "d")
screen.onkey(fun = rotateRight, key = "Right")

screen.onkey(fun = clearScreen, key = "c")
screen.listen()        

turtle.done()
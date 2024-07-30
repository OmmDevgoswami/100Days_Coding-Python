import turtle, random

turtle.colormode(255)
def randomColor():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

turt = turtle.Turtle()
screen = turtle.Screen()
screen.title ("Spirograph")
turt.speed("fastest")

def draw_spirograph(gap_length):
    for _ in range (int(360/gap_length)):
        turt.color(randomColor())
        turt.circle(100)
        turt.right(gap_length)

gap = screen.numinput("gap_length", "Enter the length of the gap: ")
draw_spirograph(gap)

turtle.done()
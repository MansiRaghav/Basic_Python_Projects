import turtle
import random
timmy = turtle.Turtle()
turtle.colormode(255)
timmy.speed("fastest")
timmy.width(1)
def color():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    my_tuple = (r, g ,b)
    return my_tuple
def spirograph(size_of_gap):
 for i in range(int(360/size_of_gap)):
     timmy.color(color())
     timmy.circle(100)
     timmy.setheading(timmy.heading() + size_of_gap)


spirograph(5)
screen = turtle.Screen()
screen.exitonclick()
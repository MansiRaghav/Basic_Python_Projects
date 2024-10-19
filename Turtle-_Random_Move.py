import turtle as t
import random

direction = [ 90,180,0,260]
timmy = t.Turtle()
t.colormode(255)

timmy.width(10) # tim.pensize()
timmy.speed("fastest")
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    my_tuple = (r,g,b) #this tuple gives random colors
    return my_tuple
for i in range(200):

  timmy.color(random_color())
  timmy.setheading(random.choice(direction))
  timmy.forward(20)
  timmy.right(random.randint(1,20))



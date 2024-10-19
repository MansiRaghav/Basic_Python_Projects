import turtle as t
import random
color = ["red","green","blue","coral","black"]
timmy = t.Turtle()

def draw_shape(num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
        timmy.forward(50)
        timmy.right(angle)




for shape_side_n in range(3,11):
 timmy.color(random.choice(color))
 draw_shape(shape_side_n)

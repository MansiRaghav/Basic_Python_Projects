
color_list = [ (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55),
               (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9)]
# 
import turtle
import random
timmy =turtle.Turtle()
turtle.colormode(255)
timmy.penup()
timmy.hideturtle()

timmy.setheading(225) 
timmy.forward(300)
timmy.setheading(0)
timmy.speed("fastest")

num_of_dots = 100
for dot_count in range(1,num_of_dots + 1):
    timmy.dot(20,random.choice(color_list))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)
my_screen = turtle.Screen()
my_screen.exitonclick()
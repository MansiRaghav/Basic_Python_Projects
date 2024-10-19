from turtle import Turtle , Screen
import random
is_race_on = False
screen = Screen()
screen.setup(height = 500,width = 500)
user_bet = screen.textinput(title = "make ur bet",prompt= "choose the winning turtle")
color =["red","orange","black","blue","purple"]
y_coordinate = [ 0,100,-100,200,-200]
all_turtles = []

for turtle_index in range(0,5):
  new_turtle = Turtle(shape="turtle")
  new_turtle.penup()
  new_turtle.color(color[turtle_index])
  new_turtle.goto(x= -230, y = y_coordinate[turtle_index])
  all_turtles.append(new_turtle)


if user_bet:
 is_race_on = True
while is_race_on:
  for turtle in all_turtles:
   if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor() # turtle.color() returns pencolor and fill color so we are choosing pencolor here
      if winning_color == user_bet:     # first argument is pencolor and second is fillcolor
         print(f"you have won,the {winning_color} turtle is thw winner")
      else:
         print(f"you have lost,the {winning_color} turtle is thw winner")
   rand_distance = random.randint(0 ,10)
   turtle.forward(rand_distance)





screen.exitonclick()
from turtle import Screen
from paddleclass import Paddle
from ballclass import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800,height = 600)
screen.title("pong")
screen.tracer(0)

r_paddle= Paddle((350,0))
l_paddle= Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down") # when fuction is used as parameter we dont use parenthesis
screen.onkey(l_paddle.go_up,"u")
screen.onkey(l_paddle.go_down,"d")
# since the screen is needed to be updated every single time we need some sort of while loop for it



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.mov_speed)
    ball.move()
    #detect collision with wall
    if ball.ycor()>280 or ball.ycor() < -280:
        ball.bounce_y()
    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or  ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()
        #detect right paddle miss
    if ball.xcor() >380 :
        ball.reset_position()
        scoreboard.l_point()
    # detect left paddle miss
    if ball.xcor()< -380 :
        ball.reset_position()
        scoreboard.r_point()












screen.exitonclick()
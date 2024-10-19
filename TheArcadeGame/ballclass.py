from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.mov_speed = 0.1

    def move(self):
        new_x = self.xcor() +self.x_move # in main function we used time to slow down each iteration
        new_y = self.ycor() + self.y_move # but to make the ball a bit slower we could have add small
        self.goto(new_x,new_y)# value such as 1 instead of 10 in the coordinate

    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1
        self.mov_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.mov_speed = 0.1
        self.bounce_x()
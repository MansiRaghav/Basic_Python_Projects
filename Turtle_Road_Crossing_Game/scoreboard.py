from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle() # why we set goto when when  we are using align in self.write?
        self.penup()      # it affects the coordinates set..as align left will point at left
        self.goto(-280,250)#of pixel while align centre point at centre of pixel
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} ", align="left", font=FONT)
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
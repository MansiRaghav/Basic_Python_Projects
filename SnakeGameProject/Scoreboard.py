from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial",24,"bold")
class Scoreboard(Turtle):
    def __init__(self):
     super().__init__()
     self.score = 0
     with open("data.txt") as data:
         self.highscore = int(data.read())

     self.color("white")
     self.penup()
     self.goto(0,260)
     self.write(arg=f"Score = {self.score}",move = False,align =ALIGNMENT,font =FONT)
     self.hideturtle()
     self.update_scoreboard()
    def update_scoreboard(self):
     self.clear() # clear should happen every time we update the scoreboard
     self.write(arg=f"Score = {self.score},High Score = {self.highscore}", move=False, align="center", font=("arial", 24, "bold"))
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",mode = "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg = "GAME OVER", move=False, align="center", font=("arial", 24, "bold"))

    def increase_score(self):
        self.score += 1
        #self.clear() this func is shifted to update scoreboard now because we are
        #geeting rid of game over func.previously we wanted to show both scores and game
        # over in the center of the screen so we coludnt put clear in update scoreboard
        # and now every time we will fail code will set our score to 0 and we wont be able to
        # see at what score we lose the game
        self.update_scoreboard()

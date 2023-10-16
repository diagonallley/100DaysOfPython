
from turtle import Turtle

class Score(Turtle):
    def __init__(self) :
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_score()

        

    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center",font=("courier", 60, "normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center", font=("courier",60,"normal"))

    def update_l_score(self):
        self.l_score+= 1
        self.update_score()

    def update_r_score(self):
        self.r_score+= 1
        self.update_score()
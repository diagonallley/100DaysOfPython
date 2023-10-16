from turtle import Turtle

ALIGNMENT="center"
FONT=("Courier",24,"normal")
class Score (Turtle):
    def __init__(self) :
        super().__init__()
        self.score=0
        with open(r'C:\Users\csona\Desktop\100DaysOfPython\day18\Snake\data.txt') as data:
            self.high_score=int(data.read())
        self.goto(0,270)
        self.penup()
        self.color('blue')
        self.update_score()
        self.hideturtle()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align=ALIGNMENT, font=(FONT,22,"normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score> self.high_score:
            self.high_score=self.score
            with open(r'C:\Users\csona\Desktop\100DaysOfPython\day18\Snake\data.txt',mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_score()
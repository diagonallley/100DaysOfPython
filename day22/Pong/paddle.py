from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self,Position) -> None:
        super().__init__()

        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(Position)
        

    def go_up(self):
        new_y=self.ycor()+20
        # print(new_y)
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y=self.ycor()-20
        # print(new_y)
        self.goto(self.xcor(),new_y)


# paddle=Paddle((0,0))

# Screen=Screen()
# Screen.listen()
# Screen.bgcolor('yellow')
# Screen.onkey(paddle.go_up,'Up')

# Screen.exitonclick()
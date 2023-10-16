from turtle import Turtle, Screen

from paddle import Paddle

from ball import Ball
from score import Score
import time

screen=Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('Pong')
screen.tracer(0)


paddle1=Paddle((350,0))
paddle2=Paddle((-350,0))
ball=Ball()
Score=Score()
game_is_on=True


screen.listen()

screen.onkey(paddle1.go_up,"Up")
screen.onkey(paddle1.go_down,"Down")
screen.onkey(paddle2.go_up,"w")
screen.onkey(paddle2.go_down,"s")


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

# Collision with top and down
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

#Collision with the paddles
    if ball.distance(paddle1)<50 and ball.xcor()>325 or ball.distance(paddle2)<50 and ball.xcor()>-325:
        ball.bounce_x()

#Detect if r_paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        Score.update_l_score()
#If left paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        Score.update_r_score()
screen.exitonclick()
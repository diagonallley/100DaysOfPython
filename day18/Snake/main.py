from turtle import Turtle, Screen

from food import Food
from score import Score
screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
starting_positions=[(0,0),(-20,0),(-40,0)]
#making squares
import time
from snake import Snake



snake=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')




game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()   
        

# Collision
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        # game_is_on=False
        # score.game_over()
        score.reset()
        snake.reset()
#Detect Collison with tail
    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment)<10:
            # game_is_on=False
            # score.game_over()
            score.reset()
            snake.reset()





screen.exitonclick()
from turtle import Turtle,Screen
from random import choice, randint
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim=Turtle()



tim.speed(5)

def random_walk(turtle):
    for i in range(1000):
        turtle.forward(25)
        color=choice(colours)
        turtle.color(color)
        number=randint(0,2)
        if number==0:
            turtle.right(90)
        else:
            turtle.left(90)

tim.pensize(10)

#random_walk(tim)
direction=[90,180,360,270,]


for i in range(200):
    tim.forward(20)
    tim.setheading(choice(direction))
    tim.color(choice(colours))






Screen=Screen()
Screen.exitonclick()
#90
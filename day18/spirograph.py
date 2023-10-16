from turtle import Turtle,Screen
from random import randint
import turtle as turtle
t=Turtle()


turtle.colormode(255)

def random_color():
    red=randint(0,255)
    green=randint(0,255)
    blue=randint(0,255)
    color=(red,green,blue)
    return color


def draw_spiro(tilt):
    for i in range(round(360/tilt)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading()+tilt)


t.speed('fastest')

draw_spiro(10)

screen=Screen()
screen.exitonclick()


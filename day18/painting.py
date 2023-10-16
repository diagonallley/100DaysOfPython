import colorgram

from turtle import Turtle, Screen
from random import choice
import turtle
# colors=colorgram.extract('..\image.jpg',32)


# rgb_colors=[]

# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)


colors_list = [ (202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41),
          (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212), (109, 123, 149), (173, 198, 205)]


tim =Turtle()
turtle.colormode(255)
tim.speed('fast')
# 10 by 10 dots
# size =20
#spacing=50
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
def draw_color(number):
    # print(color)
    for j in range(number):
        for i in range(number):
            color=choice(colors_list)

            tim.dot(20,color)
            tim.penup()
            if i<number-1:
                tim.forward(50)
            else:
                tim.left(90)
                tim.forward(50)
                tim.left(90)
                tim.forward(450)
                tim.right(90)
                tim.right(90)
            
        

draw_color(10)

Screen=Screen()
Screen.exitonclick()
from turtle import Screen, Turtle

#import turtle
#from turtle import * (everything)
tim=Turtle()
import heroes

#aliasing modules import turtle as t

print(heroes.gen())
tim.shape('turtle')

tim.color("aqua")

# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(200)
# tim.right(90)
# tim.forward(500)

def draw_square(turtle, side):
    for i in range(4):
        turtle.forward(side)
        turtle.right(90)
    
    
#draw_square(tim,100)

def dashed_line(turtle):
    for i in range (50):
        turtle.forward(5)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()

#dashed_line(tim)



def draw_triangle(turtle):
    for i in range(3):
        turtle.forward(100)
        turtle.right(120)


# def draw_pentagon(turtle):
#     for i in range(5):
#         turtle.forward(100)
#         turtle.right(72)

# def draw_hexagon(turtle):
#     for i in range(6):
#         turtle.forward(100)
#         turtle.right(60)

# def draw_heptagon(turtle):
#     for i in range(7):
#         turtle.forward(100)
#         turtle.right(180-128.57 )

# draw_triangle(tim)
# tim.color("teal")
# draw_square(tim,100)
# tim.color('green')
# draw_pentagon(tim)
# tim.color('lightgreen')
# draw_hexagon(tim)
# tim.color("blue")
# draw_heptagon(tim)


def draw_shape(turtle):
    for i in range(5,15):
        for j in range(i):
            angle=360/i
            turtle.forward(100)
            turtle.right(angle)


draw_shape(tim)



Screen=Screen()
Screen.exitonclick()
#90
#72


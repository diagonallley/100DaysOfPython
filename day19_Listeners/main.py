from turtle import Turtle, Screen

tim=Turtle()


Screen=Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counter_clockwise():
    tim.left(10)
    

def move_clockwise():
    tim.right(10)

def clear():
    tim.reset()


Screen.listen()

Screen.onkey(key="w", fun=move_forwards)
Screen.onkey(key="s", fun=move_backwards)
Screen.onkey(key="a", fun=move_counter_clockwise) #left  left
Screen.onkey(key="d", fun=move_clockwise) #right right
Screen.onkey(key="c", fun=clear) #clear drawing
Screen.exitonclick()
from turtle import Turtle, Screen
from random import choice,randint

colors=['red','orange','green','yellow','blue','purple']




all_turtles=[]
y_positions=[-70,-40,-10,20,50,80]

for turtle_index in range(0,6):
    new_turtle=Turtle('turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


is_race_on=False






Screen=Screen()
user_bet=Screen.textinput(title='Make you bet', prompt='Which turtle will win the race ')


if user_bet:
    is_race_on=True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            wining_color=turtle.pencolor()
            if wining_color==user_bet.lower():

                print(f"You have won! The {wining_color} turtle is the winner")
                 
            else:
                print(f"You have lost! The {wining_color} turtle is the winner")
                break
        rand_distance=randint(0,10)
        turtle.forward(rand_distance)
Screen.setup(height=400,width=500)
Screen.exitonclick()
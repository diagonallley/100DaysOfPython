import turtle
import pandas
screen=turtle.Screen()
screen.title('U.S States Game')
image=r"us-states-game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_guesses=0

states=pandas.read_csv(r'us-states-game\50_states.csv')
list_of_states=states["state"].to_list()
# print(states)

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
guessed_states=[]
# turtle.mainloop()
while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"{correct_guesses}/50 Guess the state",prompt="What's another state's name?").title()
    if answer_state=="Exit":
        # missing_states=[]


        missing_states=[state for state in list_of_states if state not in guessed_states]
        # for state in list_of_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    elif answer_state in list_of_states:
        correct_guesses+=1
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()

        row_state=states[states.state==answer_state]
        # print(row_state)

        # state=states["state"].item()
        x_cor=int(row_state["x"])
        y_cor=int(row_state["y"])
        t.goto(x=x_cor,y=y_cor)
        t.write(answer_state)

#states_to_learn.csv generate

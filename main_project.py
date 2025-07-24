import pandas
import  turtle
screen=turtle.Screen()
# screen.setup(width=600,height=600)
screen.title("guessing us-state game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
all_state=states_data_names=pandas.read_csv("50_states.csv").state
guessed_state=[]
while len(guessed_state)<50:
    answer_state=screen.textinput(title=f"{len(guessed_state)}/50 are guessed state",prompt="what's the name of the state").title()
    data=pandas.read_csv("50_states.csv")
    states_data_names=pandas.read_csv("50_states.csv").state
    state_dict=states_data_names.to_list()
    # last step to show players trick to exit out and then show the
    # the state they skipped and print new csv file to show what they missed
    if answer_state=="Exit":
        missing_state=[]
        for any_state in all_state:
            if any_state not in guessed_state:
                missing_state.append(any_state)
                missing_states_after_guess=pandas.DataFrame(missing_state)
                missing_states_after_guess.to_csv("missing_states_after_guess.csv")
                print(missing_states_after_guess)


        # using list comprehension only two lines are enough
        missing_state=[state for state in all_state if state not in guessed_state ]
        print(pandas.DataFrame(missing_state).to_csv("missing_state_using_list_comprehension.csv"))


        break
    if answer_state in state_dict:
        guessed_state.append(answer_state)
        tim=turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_position=data[states_data_names==answer_state]
        tim.goto(state_position.x.item(),state_position.y.item())
        tim.write(answer_state)

# creating csv file containing all states



# locating coordinate on map
# def get_mouse_onclick_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_onclick_coor)
# turtle.mainloop()

screen.exitonclick()

##Importing Modules...
import turtle
import pandas


##Display and Game Algorithms
screen = turtle.Screen()
screen.title("U.S. State Game")

#Adding turtle shape
image = "blank_states_img.gif"   #Filename of the image
screen.addshape(image)  #Adds the image as a shape
turtle.shape(image)


##CSV Algorithms
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []


while len(guessed_state) < 50:

    answer_state = screen.textinput(title= f"{len(guessed_state)}/50 States Correct!",
                                    prompt= "Name a state: ").title()

    # print(answer_state)

    if answer_state in all_states and answer_state not in guessed_state:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guessed_state.append(answer_state)

    if answer_state == "Exit":
        # #Alternative listed below
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_states.append(state)

        missing_states = [state for state in all_states if state not in guessed_state]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missed_states.csv")
        break


#States to csv (Only the ones that have not been guessed by the user


# #Gets mouse click coordinates on turtle (Stackoverflow)
# def get_mouse_click_coordinate(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coordinate)
# turtle.mainloop()



# screen.exitonclick()  #Disabled temporarily for the coordinates
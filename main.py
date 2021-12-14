from turtle import Turtle, Screen
import pandas
turtle = Turtle()
screen = Screen()
screen.title("U.S STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_given = screen.textinput(title=f"{len(guessed_states)}/50 states guessed right",
                                    prompt="Guess another state").title()

    if answer_given == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_study.csv")
        break

    if answer_given in all_states:
        guessed_states.append(answer_given)
        state_data = data[data.state == answer_given]
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_given)









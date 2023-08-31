import turtle, pandas
from state_name import StateName

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_list = states_data["state"].to_list()
right_guesses = []

while len(right_guesses) < 50:
    answer_text = screen.textinput(title=f"{len(right_guesses)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_text == "Exit":
        missing_states = list(set(states_list) - set(right_guesses))
        df = pandas.DataFrame(sorted(missing_states))
        df.to_csv("missing_states.csv")
        break
    if answer_text in states_list:
        state = states_data[states_data.state == answer_text]
        x = int(state.x.iloc[0])
        y = int(state.y.iloc[0])
        right_state = StateName(state=answer_text, x=x, y=y)
        right_guesses.append(answer_text)

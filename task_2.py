import turtle


def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    num_turns = 5

    if state == "finish":
        t.setheading(180)
        t.forward(10*turn)  # MoveLeft

        if True:
            state = "end"
            return state, turn
        return state, turn
    if state == "init":

        if True:
            state = "left"
            return state, turn
        return state, turn
    if state == "left":
        t.setheading(180)
        t.forward(10*turn)  # MoveLeft

        if turn < num_turns:
            state = "down"
            return state, turn
        return state, turn
    if state == "right":
        t.setheading(0)
        t.forward(10*turn)  # MoveRight

        if turn < num_turns:
            state = "up"
            return state, turn
        return state, turn
    if state == "up":
        t.setheading(90)
        t.forward(10*turn)
        turn += 1  # MoveUp

        if turn == num_turns:
            state = "finish"
            return state, turn
        if turn < num_turns:
            state = "left"
            return state, turn
        return state, turn
    if state == "down":
        t.setheading(270)
        t.forward(10*turn)
        turn += 1  # MoveDown

        if turn < num_turns:
            state = "right"
            return state, turn
        return state, turn
    return state, turn


def draw():
    start_state = "init"
    end_state = "end"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(0)
    turn = 1

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)
    turtle.done()


if  __name__ == "__main__":
    draw()

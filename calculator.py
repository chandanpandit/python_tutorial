# a basic calculator

from tkinter import *
from functools import partial

# methods


def append_input(num):
    input_field.insert(END, num)


def reset():
    input_field.delete(0, END)


def evaluate():
    print("Evaluating expression")
    try:
        result = eval(input_field.get())
    except (NameError, SyntaxError):
        result = "Syntax Error"
    print(result)
    strvar.set(result)


def create_result_label(window, strvarlabel):
    l = Label(window, textvariable=strvarlabel)
    l.pack()
    return l


def create_numpad(window):
    num_pad = []
    for number in range(1, 10):
        print("Creating Button"+str(number))
        num_button = Button(window, text=str(number), command=partial(append_input, number))
        num_pad.append(num_button)
        num_button.pack()
    return num_pad


def create_operator_buttons(window):
    operator_buttons = ["+", "-", "*", "/", "^"]
    for btn in operator_buttons:
        Button(window, text=btn, command=partial(append_input, btn)).pack()


def create_control_buttons(window):
    # control buttons
    Button(window, text="=", command=evaluate).pack()
    Button(window, text="CLEAR", command=reset).pack()


def render_calculator(window, strvarlabel):
    create_result_label(window, strvarlabel)
    create_numpad(window)
    create_operator_buttons(window)
    create_control_buttons(window)

# methods end


root = Tk()
Label(root, text="My Calculator").pack()
input_field = Entry(root, width=10)
input_field.pack()

strvar = StringVar()
strvar.set("_______________")

render_calculator(root, strvar)

root.mainloop()



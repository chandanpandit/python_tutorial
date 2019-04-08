from tkinter import *
from tkinter import messagebox
from functools import partial


# draw ui
def draw(window):
    buttons = []
    for row in range(3):
        row_buttons = []
        for column in range(3):
            btn = Button(window, text="", bg="white", command=partial(cut, row, column))
            btn.grid(row=row, column=column, ipadx=30, ipady=30)
            row_buttons.append(btn)
        buttons.append(row_buttons)
    return buttons


def cut(row, column):
    global turn
    if matrix[row][column] == 0:
        mark = "X" if turn == 1 else "0"
        color = "red" if turn == 1 else "blue"
        matrix[row][column] = 1 if turn == 1 else 2
        all_buttons[row][column].configure(text=mark, bg=color)
        winner = check_winner()
        if winner != 0:
            messagebox.showinfo("Congratulation!", "Player "+str(turn)+" won.")
            reset_game()
        else:
            turn = 2 if turn == 1 else 1  # change turn
    else:
        messagebox.showerror("Cell already selected", "Please select an empty cell.")


def check_winner():
    global turn
    for row in range(3):
        if matrix[row][0] == turn and matrix[row][1] == turn and matrix[row][2] == turn:
            return turn
    for column in range(3):
        if matrix[0][column] == turn and matrix[1][column] == turn and matrix[2][column] == turn:
            return turn
    if (matrix[0][0] == turn and matrix[1][1] == turn and matrix[2][2] == turn) \
            or (matrix[0][2] == turn and matrix[1][1] == turn and matrix[2][0] == turn):
        return turn
    return 0


def reset_game():
    for row in range(3):
        for column in range(3):
            matrix[row][column] = 0
            all_buttons[row][column].configure(text="", bg="white")


root = Tk()
turn = 1
all_buttons = draw(root)
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

root.mainloop()

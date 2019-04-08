from tkinter import *
from tkinter import  messagebox

# prints table of given number


def update_table():
    try:
        number = int(entry.get())
        for i in range(10):
            line = str(number) + " X " + str(i + 1) + " = " + str(number * (i + 1))
            table[i].set(line)
    except ValueError:
        messagebox.showerror(title="Invalid Number", message="Please enter a valid number")
        

root = Tk()

entry = Entry(root)
entry.pack()
button = Button(root, text="Print Table", command=update_table)
button.pack()

table = []
for j in range(10):
    table.append(StringVar())
    color = "red" if j % 2 == 0 else "yellow"
    Label(root, textvar=table[j], bg=color).pack()

root.mainloop()


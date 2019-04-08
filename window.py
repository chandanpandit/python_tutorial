from tkinter import *
from tkinter import messagebox

print("Learning to create window programs")
# shows usage of different window components

root = Tk()

# Label Demo

label1 = Label(root, text="Hello!")
label2 = Label(root, text="Hello Chandan !")

label1.pack()
label2.pack()

# Message Box Demo


def click_action():
    print("Hello")
    messagebox._show("Hello", "Hello From Chandan")


button = Button(root, text="Click Me", command=click_action)
button.pack()

# buttton click action demo


def turn_red():
    variableLabel.set("Red")
    label3.config(bg="red")


def turn_green():
    variableLabel.set("Green")
    label3.config(bg="green")


def turn_blue():
    variableLabel.set("Blue")
    label3.config(bg="blue")


variableLabel = StringVar();
variableLabel.set("White")
label3 = Label(root, textvar=variableLabel)
label3.pack()
redButton = Button(root, text="Red", command=turn_red).pack()
greenButton = Button(root, text="Green", command=turn_green).pack()
blueButton = Button(root, text="Blue", command=turn_blue).pack()

# form elements
Label(root, text="Fill This form").pack()
Label(root, text="Name : ").pack()
nameEntry = Entry(root, bg='yellow')
nameEntry.pack()

Label(root, text="Your choices : ").pack()
Checkbutton(root, text="Milk").pack()
Checkbutton(root, text="Coffee").pack()
Checkbutton(root, text="Tea").pack()
Checkbutton(root, text="Biscuits").pack()

greetingText = StringVar()
greetingText.set("_________________")

greetingEntry = Entry(root)
greetingEntry.pack()


def reset_text():
    greetingEntry.delete(0, END)


def update_greeting():
    greetingText.set(greetingEntry.get())


label4 = Label(root, textvariable=greetingText)
label4.pack()
Button(root, text="Reset Name", command=reset_text).pack()
Button(root, text="Update Name", command=update_greeting).pack()

gender = StringVar()


def print_gender():
    print(gender.get())


Radiobutton(root, text="Male", value="M", variable=gender).pack()
Radiobutton(root, text="Female", value="F", variable=gender).pack()
Button(root, text="Show Selected Gender", command=print_gender).pack()

root.mainloop()


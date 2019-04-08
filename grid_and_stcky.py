from tkinter import *

print("Learning Positioning widgits into grid")

root = Tk()

label1 = Label(root, text="Label 1", bg="red")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = Label(root, text="Label 2", bg="blue")
label2.grid(row=0, column=1, ipadx=10, ipady=10)

label3 = Label(root, text="Label 3", bg="green")
label3.grid(row=1, column=0, sticky=W+E)

label4 = Label(root, text="Label 4", bg="yellow")
label4.grid(row=1, column=1, ipadx=10, ipady=10)

label5 = Label(root, text="Label 5", bg="orange")
label5.grid(row=2, column=0, ipadx=10, ipady=10)

label6 = Label(root, text="Label 6", bg="red")
label6.grid(row=2, column=1, sticky=N+S)

label7 = Label(root, text="Label 7", bg="magenta")
label7.grid(row=3, column=0, sticky=SW)

label8 = Label(root, text="Label 8", bg="pink")
label8.grid(row=3, column=1, ipadx=10, ipady=10)

root.mainloop()

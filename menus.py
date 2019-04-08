from tkinter import *

print("Leaning to add menus in GUI application using tkinter lib")


def openClicked():
    print("Open Was Clicked")


def exitClicked():
    print("Exiting the application")
    quit()


def copyClicked():
    print("Copy Was Clicked")


def pasteClicked():
    print("Paste Was Clicked")


def undoClicked():
    print("Undo Was Clicked")


def redoClicked():
    print("Redo Was Clicked")


root = Tk()

menu = Menu(root)
root.configure(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=openClicked)
subMenu.add_command(label="Exit", command=exitClicked)

subMenu2 = Menu(menu, tearoff=0)  # tearoff removes the ---- from menu
menu.add_cascade(label="Edit", menu=subMenu2)
subMenu2.add_command(label="Copy (Ctrl + C)", command=copyClicked)
subMenu2.add_command(label="Paste (Ctrl + V)", command=pasteClicked)
subMenu2.add_separator()  # add a separator when you want to separate two groups of menus
subMenu2.add_command(label="Undo", command=undoClicked)
subMenu2.add_command(label="Redo", command=redoClicked)


root.mainloop()

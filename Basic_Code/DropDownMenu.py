from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Drop Down Menu")
root.geometry("200x200")

def show():
    label = Label(root, text=clicked.get()).pack()

#Creating Drop Down Menu
#Option list is the list for the option in drop
# we use * before the name of variable list
# for take all value in list
#clicked.set is to show default value
option = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
clicked = StringVar()
clicked.set(option[0])
drop = OptionMenu(root, clicked, *option)
drop.pack()

my_btn = Button(root, text = "Show Drop", command = show).pack()

mainloop()
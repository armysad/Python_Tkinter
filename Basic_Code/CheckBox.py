from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Check Box")
root.geometry("200x200")

var = StringVar()

def check():
    label = Label(root, text = var.get()).pack()
    if var.get() == "Supersize":
        root.geometry("500x500")
    elif var.get() == "Normal":
        root.geometry("200x200")

#Creating Check Button
#deselect is for not checking the checkbutton for the first time
c = Checkbutton(root, text = "Check This Box", variable = var, onvalue = "Supersize", offvalue = "Normal")
c.deselect()
c.pack()

my_btn = Button(root, text = "Show Selection", command = check).pack()

mainloop()
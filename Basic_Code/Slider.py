from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Slider")
root.geometry("400x400")

#Function for slider
def slide(var):
    my_label = Label(root, text = horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

#Create Slider
vertical = Scale(root,from_=200, to = 400, command = slide)
vertical.pack()

horizontal = Scale(root,from_=200, to = 400, orient = HORIZONTAL, command =slide)
horizontal.pack()

mainloop()
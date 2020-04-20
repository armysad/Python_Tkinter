from tkinter import *

root = Tk()

#create a label widget
mylabel1 = Label(root,text="Hello World")
mylabel2 = Label(root,text="My name is Rafii")

#grid
mylabel1.grid(row = 0,column = 0)
mylabel2.grid(row = 0,column = 1)

#Looping screen
root.mainloop()

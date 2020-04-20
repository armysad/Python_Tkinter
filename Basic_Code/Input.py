from tkinter import *

root = Tk()
root.title("Learn Tkinter")

#Creating Input
e = Entry(root)
e.grid(row=0,column=0)

#Creting Function to command Button
def mybutton():
    mylabel = Label(root,text = "Hello "+e.get())
    mylabel.grid(row=3,column=0)

#Creating Button
mybutton = Button(root,text="Submit",command=mybutton)
mybutton.grid(row=1,column=0)

#Looping screen
root.mainloop()

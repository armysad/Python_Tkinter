from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio Button")

#Variable for Radio Button
r = IntVar()
r.set("2")
pizza = StringVar()
pizza.set("Pepperoni")

#list for loop radio button
Modes = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion")
]

#Creating Radio Button using loop
for text,mode in Modes:
    Radiobutton(root, text = text, variable = pizza, value = mode).pack(anchor = W)

#Function for loop
def clicked(value):
    mylabel = Label(root, text=pizza.get())
    mylabel.pack(anchor = E)

#Function for Manual
def clicked2(value):
    mylabel2 = Label(root, text=r.get())
    mylabel2.pack(anchor = W)

#Creting Radio Button Manual
Radiobutton(root, text = "Option 1", variable = r, value = 1,command = lambda:clicked2(r.get())).pack()
Radiobutton(root, text = "Option 2", variable = r, value = 2,command = lambda:clicked2(r.get())).pack()

mylabel = Label(root, text = pizza.get())
mylabel.pack(anchor =E)
mylabel2 = Label(root, text = r.get())
mylabel2.pack(anchor = W)

mybutton = Button(root, text = "Appear the Value", command = lambda: clicked(pizza.get()))
mybutton.pack(anchor =W)

root.mainloop()
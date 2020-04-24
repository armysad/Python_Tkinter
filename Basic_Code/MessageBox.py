from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

root = Tk()
root.title("Message Box")

#Show info
def popup():
    # return dari showinfo warning hanya 'ok'
    response = messagebox.showinfo("Error", "Hello World")
    Label(root, text=response).pack()

#Show Warninng
def warning():
    # return dari response warning hanya 'ok'
    response = messagebox.showwarning("Warning", "Hello world")
    Label(root, text=response).pack()

#Show Error
def error():
    #return dari response error hanya 'ok'
    response = messagebox.showerror("Warning", "Hello world")
    Label(root, text = response).pack()

#askquestion
def question():
    # return dari response question adalah "yes" or 'no'
    response = messagebox.askquestion("Warning", "Hello world")
    if response == "yes":
        Label(root, text = "You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No!").pack()

#ask ok cancel
def askokcancel():
    #return dari response ask yes no adalah 1 atau 0
    # 1 berarti 'yes' dan 0 berarti 'no'
    response = messagebox.askokcancel("Warning", "Hello world")
    if response == 1:
        Label(root, text = "You Clicked Ok!").pack()
    else:
        Label(root, text="You Clicked Cancel!").pack()

#ask yes no
def yesno():
    response = messagebox.askyesno("Warning", "Hello world")
    #return dari response ask yes no adalah 1 atau 0
    # 1 berarti 'yes' dan 0 berarti 'no'
    if response == 1:
        Label(root, text = "You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No!").pack()

Button(root, text = 'pop Up', command =popup).pack()


mainloop()
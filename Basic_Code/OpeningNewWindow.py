from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Opening New Window")

def openwindow():
    #Buat global variable untuk img
    #agar bisa dibaca oleh root
    global img
    # Creating New Window
    top = Toplevel()
    top.title("New Window")
    img = ImageTk.PhotoImage(Image.open("Image/gambar-bunga-sepatu.jpg"))
    label = Label(top, image=img).pack()
    btn = Button(top,text = "Close window", command = top.destroy).pack()

button = Button(root, text = "Open New Window", command = openwindow)
button.pack()

mainloop()
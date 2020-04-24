from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.title("Dialog Box Files")

def openfile():
    global my_image,my_btn
    #Creating Dialog Box Files
    name = filedialog.askopenfilename(initialdir = "../Project/Image", title = "Select File",filetypes = (("jpg files", "*.jpg"),("all files", "*.*")))
    my_label = Label(root, text = name).pack()
    my_image =ImageTk.PhotoImage(Image.open(name))
    my_image_label = Label(image = my_image).pack()

my_btn = Button(root, text = "Open Files", command = openfile).pack()


mainloop()
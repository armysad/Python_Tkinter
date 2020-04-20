from tkinter import *
#library untuk memasukan image
#yang di install libnya adalah lib Pillow
#karena Lib Pillow adalah upgrade-an dari lib PIL
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Tkinter")

#Change Icon
root.iconbitmap('C:/Users/Rajwa/Documents/Rafii/Python/Tkinter/Basic_Code/fb.ico')

#Create Image
#To Create Image needs 3 step
#1. Define the Image
#2. Put the Define Into Variable
#3. Put The Variable into Label Variable

#Step2       Step1
my_img=ImageTk.PhotoImage(Image.open("gambar-bunga-sepatu.jpg"))
#Step3
my_label = Label(image = my_img)


#Creating button
button_quit = Button(root, text = 'Quit', command = root.quit)

#Positioning
my_label.pack()
button_quit.pack()


#Looping screen
root.mainloop()

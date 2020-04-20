from tkinter import *

root = Tk()

#create function yang dipanggil setelah click button
def myclick():
    mylabel = Label(root, text = "mantap",fg="Red")
    mylabel.pack()

#Creating button
#State berguna untuk mengatur tombol NORMAL, ACTIVE, atau DISABLE
#padx dan pady mengatur besar dan lebar button
#Command untuk memanggil function setelah mengclick button
#fg untuk mewarnai huruf
#bg background
mybutton = Button(root, text = "Click me", command = myclick, fg="Blue", bg="Grey")

mybutton.pack()

#Looping screen
root.mainloop()

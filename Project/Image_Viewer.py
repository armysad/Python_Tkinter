from tkinter import *
#library untuk memasukan image
#yang di install libnya adalah lib Pillow
#karena Lib Pillow adalah upgrade-an dari lib PIL
from PIL import ImageTk, Image

root =Tk()
root.title("Image Viewer")

#Create Image
my_img1 = ImageTk.PhotoImage(Image.open('Image/1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('Image/2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('Image/3.jpeg'))
my_img4 = ImageTk.PhotoImage(Image.open('Image/4.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('Image/5.jpg'))
img_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

my_label = Label(image=my_img1)

#Creating Status Bar
status = Label(root, text = "image 1 of " + str(len(img_list)), bd = 1, relief = SUNKEN, anchor = E)


def forward(img_number):
    global my_label,button_next,button_back

    my_label.grid_forget()
    my_label = Label(image = img_list[img_number - 1])
    button_next = Button(root,text = '>>', command = lambda :forward(img_number + 1))
    button_back = Button(root,text = '<<', command = lambda: back(img_number-1))
    if img_number == len(img_list):
        button_next = Button(root,text='>>', state = DISABLED)
    my_label.grid(row=0,column=0,columnspan=3)
    button_next.grid(row=1,column=2)
    button_back.grid(row=1, column=0)
    status = Label(root, text="image "+str(img_number) +" of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

def back(img_number):
    global my_label,button_forward,button_back
    my_label.grid_forget()
    my_label = Label(image = img_list[img_number - 1])
    button_next = Button(root,text = '>>', command = lambda :forward(img_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(img_number - 1))
    if img_number == 1:
        button_back = Button(root,text = '<<', state = DISABLED)
    my_label.grid(row=0,column=0,columnspan=3)
    button_next.grid(row=1,column=2)
    button_back.grid(row=1, column=0)
    status = Label(root, text="image "+str(img_number) +" of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

#Create Button
button_back = Button(root,text = '<<', command = back,state = DISABLED)
button_next = Button(root,text = '>>', command = lambda :forward(2))
button_quit = Button(root,text ='Quit', command = root.quit)

#Create Position
my_label.grid(row=0,column=0,columnspan=3)
button_back.grid(row=1,column = 0)
button_quit.grid(row=1,column=1)
button_next.grid(row=1,column=2)
status.grid(row = 2, column = 0,columnspan = 3, sticky = W+E)#W adalah west and E adalah East, jadi sticki akan berjalan dari west ke east

#Looping screen
root.mainloop()

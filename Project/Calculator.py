from tkinter import *

root = Tk()
root.title("Simple Calculator")

#Creating Input
e = Entry(root,width = 30, borderwidth = 1.5)
e.grid(row = 0,column =0,columnspan = 3, padx = 40, pady = 10)

#Creating function for command button
def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def sign(tanda):
    first_number = e.get()
    global f_num, sgn
    f_num = int(first_number)
    sgn = tanda
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if sgn == "+":
        e.insert(0, f_num + int(second_number))
    elif sgn == "*":
        e.insert(0, f_num * int(second_number))
    elif sgn == "/":
        e.insert(0, f_num/int(second_number) )
    elif sgn == "-":
        e.insert(0,f_num-int(second_number) )


#Creating button
button_1 = Button(root, text = '1', padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = '2', padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = '3', padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = '4', padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = '5', padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = '6', padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = '7', padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = '8', padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = '9', padx = 40, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = '0', padx = 40, pady = 20, command = lambda: button_click(0))
button_00 = Button(root, text = '00', padx = 37, pady = 20, command = lambda: button_click('00'))
button_t = Button(root, text = '000', padx = 34, pady = 20, command = lambda: button_click('000'))
button_add = Button(root, text = '+', padx = 40, pady = 20, command = lambda: sign("+"))
button_kurang = Button(root, text = '-', padx = 40, pady = 20, command = lambda: sign("-"))
button_kali = Button(root, text = 'x', padx = 40, pady = 20, command = lambda: sign("*"))
button_bagi = Button(root, text = ':', padx = 40, pady = 20, command = lambda: sign("/"))
button_equal = Button(root, text = '=', padx = 88, pady = 20, command = button_equal)
button_clear = Button(root, text = 'C', padx = 88, pady = 20, command = button_clear)

#Positioning
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_00.grid(row=4,column=1)
button_t.grid(row=4,column=2)

button_clear.grid(row=5,column=0,columnspan = 2)
button_add.grid(row=1,column=3)
button_kurang.grid(row = 2, column = 3)
button_kali.grid(row = 3, column = 3)
button_bagi.grid(row = 4, column = 3)
button_equal.grid(row=5,column=2,columnspan = 2)


#Looping screen
root.mainloop()


from tkinter import *

root = Tk()
root.title('Menu System')
root.iconbitmap('bird.ico')
root.geometry('500x340')

value1 = 0
value2 = 0
value3 = 0

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var1.set(0)
var2.set(0)
var3.set(0)

check_10pass = Checkbutton(root, variable=var1, text='Class 10 pass')
check_12pass = Checkbutton(root, variable=var2, text='Class 12 pass')
check_graduate = Checkbutton(root, variable=var3, text='Graduate')
check_10pass.pack()
check_12pass.pack()
check_graduate.pack()

def show():
	global value1
	global value2
	global value3
	global lbl_result
	value1 = var1.get()
	value2 = var2.get()
	value3 = var3.get()
	lbl_result.config(text='10 Pass = '+str(value1)+' / 12 Pass = '+str(value2)+' / Graduate = '+str(value3))

btn_value = Button(root, text='Click to see the value', command=show)
btn_value.pack()

lbl_result = Label(root, text='10 Pass = '+str(value1)+'/ 12 Pass = '+str(value2)+'/ Graduate = '+str(value3))
lbl_result.pack(pady=25)

root.mainloop()

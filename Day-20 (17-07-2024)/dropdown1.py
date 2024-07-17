from tkinter import *

root = Tk()
root.title('Dropdown Box')
root.iconbitmap('bird.ico')
root.geometry('500x340')

clicked = StringVar()
clicked.set('Red')

drop_down = OptionMenu(root, clicked, 'White','Black','Red','Green','Blue','Yellow')
drop_down.pack()

lbl_result = Label(root, text='...')

def show():
	global lbl_result
	global clicked
	lbl_result.config(text=clicked.get())

btn_click = Button(root, text='Click to view the choice', command=show).pack(pady=10)

lbl_result.pack(pady=40)

root.mainloop()

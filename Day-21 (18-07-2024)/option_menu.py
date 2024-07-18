from tkinter import *

root = Tk()
root.title('Dropdown Box')
root.iconbitmap('bird.ico')
root.geometry('500x340')

options = (
	'COBOL',
	'BASIC',
	'Algol',
	'Pascal',
	'ForTran',
	'Java',
	'Python',
	'JavaScript',
	'C++'
)

clicked = StringVar()
clicked.set(options[0])

drop_down = OptionMenu(root, clicked, *options)
drop_down.pack()

lbl_result = Label(root, text='...')

def show():
	global lbl_result
	global clicked
	lbl_result.config(text=clicked.get())

btn_click = Button(root, text='Click to view the choice', command=show).pack(pady=10)

lbl_result.pack(pady=40)

root.mainloop()

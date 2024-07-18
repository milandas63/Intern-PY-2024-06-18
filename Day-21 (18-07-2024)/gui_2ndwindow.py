from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Menu System')
root.iconbitmap('images/bird.ico')
#root.geometry('310x240')

title = Label(root, text='Main Window').pack()
Label(root, text=' ').pack()

img_obj1 = ImageTk.PhotoImage(Image.open('images/goodmorning1.jpg').resize((300,205), Image.LANCZOS))
img_obj2 = ImageTk.PhotoImage(Image.open('images/goodmorning2.jpg').resize((300,205), Image.LANCZOS))
img_obj3 = ImageTk.PhotoImage(Image.open('images/goodmorning3.jpg').resize((300,205), Image.LANCZOS))
img_obj4 = ImageTk.PhotoImage(Image.open('images/goodmorning4.jpg').resize((300,205), Image.LANCZOS))
img_obj5 = ImageTk.PhotoImage(Image.open('images/goodmorning5.jpg').resize((300,205), Image.LANCZOS))
img_obj6 = ImageTk.PhotoImage(Image.open('images/goodmorning6.jpg').resize((300,205), Image.LANCZOS))
img_obj7 = ImageTk.PhotoImage(Image.open('images/goodmorning7.jpg').resize((300,205), Image.LANCZOS))

index = -1
img_list = [img_obj1,img_obj2,img_obj3,img_obj4,img_obj5,img_obj6,img_obj7]


def previous_pic():
	global index
	global img_list
	global my_label
	global new_window
	index = index - 1
	if index<0:
		index = 6

	my_label = Label(new_window,image=img_list[index])
	my_label.grid(row=0,column=0,columnspan=3)
	
def next_pic():
	global index
	global img_list
	global my_label
	global new_window
	index = index + 1
	if index>6:
		index = 0

	my_label = Label(new_window,image=img_list[index])
	my_label.grid(row=0,column=0,columnspan=3)

def window():
	global index
	global new_window

	index = -1
	new_window = Toplevel()
	new_window.title('Image Gallery')
	new_window.iconbitmap('images/bird.ico')
	new_window.geometry('310x240')

	next_pic()
	btn_previous = Button(new_window, text='Previous Photo', command=previous_pic)
	btn_next = Button(new_window, text='Next Photo', command=next_pic)
	btn_close = Button(new_window, text='Exit Program', command=new_window.destroy)

	btn_previous.grid(row=2, column=0)
	btn_next.grid(row=2, column=1)
	btn_close.grid(row=2, column=2)

btn_next_window = Button(root, text='Image Gallery', bg='#AAAAAA', command=window)
btn_next_window.pack(pady=30,padx=20)

root.mainloop()


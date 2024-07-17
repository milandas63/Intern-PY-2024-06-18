from tkinter import *

root = Tk()
root.title('Login')

def showdata():
	username = tf_username.get()
	password = tf_password.get()
	lbl_show.config(text='Username: '+username+', password: '+password)

lbl_username = Label(root, text='Username:')
lbl_username.grid(row=0, column=0, columnspan=3)

tf_username = Entry(root,width=50)
tf_username.grid(row=1, column=0, columnspan=3)

lbl_password = Label(root, text='Password:')
lbl_password.grid(row=2, column=0, columnspan=3)

tf_password = Entry(root,width=50)
tf_password.grid(row=3, column=0, columnspan=3)

lbl_dummy1 = Label(root, text='')
lbl_dummy1.grid(row=4,column=1)
lbl_dummy2 = Label(root, text='')
lbl_dummy2.grid(row=5,column=1)

btn_login = Button(root, text=' Login ', padx=20, command=showdata)
btn_login.grid(row=6, column=0)

lbl_dummy2 = Label(root, text='', width=50)
lbl_dummy2.grid(row=7,column=0)

lbl_show = Label(root, text='')
lbl_show.grid(row=8, column=0)

root.mainloop()

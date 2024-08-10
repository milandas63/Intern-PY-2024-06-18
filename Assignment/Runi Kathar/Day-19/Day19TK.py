
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap("bird.ico")
root.title("Python GUI program")
root.geometry("500x400")

w = Label(root, text='  Hello World!  ', 
          font='40', pady='15', padx='50',
          bg='blue', fg='yellow', bd='5', width='200')
w.pack()

frame1 = Frame(root)
frame1.pack()
b1_button = Button(frame1, text =" Free Hand Button ", fg ="red")
b1_button.pack(side=LEFT)
b2_button = Button(frame1, text =" Project Button ", fg ="blue")
b2_button.pack(side=LEFT)
b3_button = Button(frame1, text =" Rectangular Button ", fg ="green")
b3_button.pack(side=LEFT)


frame2 = Frame(root)
frame2.pack(side=BOTTOM)
t1_button = Button(frame1, text =" Free Hand Button ", fg ="yellow")
t1_button.pack(side=BOTTOM)
t2_button = Button(frame1, text =" Project Button ", fg ="orange")
t2_button.pack(side=BOTTOM)
t3_button = Button(frame1, text =" Rectangular Button ", fg ="violet")
t3_button.pack(side=BOTTOM)


root.mainloop()

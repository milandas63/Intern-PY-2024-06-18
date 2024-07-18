from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Like Internal Frame')
root.iconbitmap('images/bird.ico')

frame = LabelFrame(root, text='Call started...', padx=50, pady=50)
frame.pack(padx=10, pady=10)

btn_view = Button(frame, text='Click to View')
btn_show = Button(frame, text='Click to start')
btn_sample = Button(frame, text='Click to close')
btn_view.grid(row=0,column=0)
btn_show.grid(row=2,column=1)
btn_sample.grid(row=2,column=2)

root.mainloop()


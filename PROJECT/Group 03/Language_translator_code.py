from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Initialize the main window
root = Tk()
root.geometry('1080x400')
root.resizable(0, 0)
root.config(bg='ghost white')
root.title("Language Translator")

# Add title and label
Label(root, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg='white smoke').pack()
Label(root, text="Python Project", font='arial 15 bold', bg='white smoke', width='20').pack(side='bottom')
Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=200, y=60)

# Input text box
Input_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Input_text.place(x=30, y=100)

# Output text box
Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=60)
Output_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Output_text.place(x=600, y=100)

# Language selection dropdowns
language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values=language, width=22)
src_lang.place(x=20, y=60)
src_lang.set('choose input language')

dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=890, y=60)
dest_lang.set('choose output language')

# Translation function
def Translate():
    translator = Translator()
    src_language = src_lang.get()
    dest_language = dest_lang.get()
    src_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(src_language)]
    dest_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(dest_language)]
    text = Input_text.get(1.0, END)
    translated = translator.translate(text, src=src_code, dest=dest_code)

    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

# Translate button
trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='royal blue1', activebackground='sky blue')
trans_btn.place(x=490, y=180)

# Run the main loop
root.mainloop()

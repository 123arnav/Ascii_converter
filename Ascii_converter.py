# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 11:24:30 2021

@author: email
"""
from tkinter import*
root=Tk()
root.title("Ascii converter")
root.geometry("400x400")
root.configure(background="CadetBlue1")
enter_word=Entry(root)
enter_word.place(relx=0.5, rely=0.6, anchor=CENTER)
name=Label(root,text="Name In Ascii: ",bg="SlateBlue1",fg="CadetBlue1")
def AsciiConverter():
    input_word=enter_word.get()
    for letter in input_word:
        name["text"]+=str(ord(letter))+" "
btn=Button(root,text="Convert",command=AsciiConverter,bg="SlateBlue1",fg="CadetBlue1")
btn.place(relx=0.5, rely=0.8, anchor=CENTER)
name.place(relx=0.5, rely=0.7, anchor=CENTER)
root.mainloop()

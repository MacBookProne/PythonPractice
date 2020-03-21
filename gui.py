#!/usr/bin/python

import Tkinter
import tkMessageBox

top = Tkinter.Tk("button")
# Code to add widgets will go here...

top.geometry("500x500")



def helloCallBack():

   tkMessageBox.showinfo( "Hello Python", "Hello World")


j = Tkinter.Button(top, text ="Hello", command = helloCallBack, height = 50, width = 50)
#j = Tkinter.Button(top, text = "Send", height = 100, width = 100)







j.pack()
top.mainloop()

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 22:53:48 2022

@author: User
"""

#!/usr/bin/python

from tkinter import *

root = Tk()
root.title("Baghbondi khela")
root.geometry("900x900")

class ui:
    def __init__(self,root):
        myFrame = Frame(root)
        myFrame.pack()
        photo = PhotoImage(file = "board.png")
        label = Label(root, image=photo)
        label.pack()
e = ui(root)

root.mainloop()
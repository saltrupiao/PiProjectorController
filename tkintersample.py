#!/usr/bin/python

from Tkinter import *

class App:

    def __init__(self):
        self.root = Tk()
        self.root.title("Notpad")
        self.root.minsize(width=500,height=400)
                
        # Set up basic Menu
        menubar = Menu(self.root)

        menubar.add_command(label="Button")
        
        self.root.config(menu=menubar)

app = App()

app.root.mainloop()

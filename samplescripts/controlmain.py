import sys
import os

from tkinter import *
import tkinter as tk

#def mmWindow():
#    mmWindow = tk.Tk()
#    mmWindow.geometry('800x480')

def powerOn():
    os.system('opencv_video.py')

mWindow = tk.Tk
mWindow.geometry('800x400')
mWindow.title('A/V Control - Media Center')

wtitle = Label(mWindow, text="Media Center A/V Controller", fg='blue')
wtitle.grid(row=0, column=6)

#------Images------
#powerOnImage = PhotoImage(file="images/power_on.gif")

btnPowerOn = Button(mWindow, command=powerOn(), height=50, width=150)
#btnPowerOn.config(image=powerOnImage)
btnPowerOn.grid(row=1, column=1)

# Button opens an additional window
#mmbutton = tk.Button(mWindow, height=5, width=20, text="Main Menu", command=mmWindow)
#mmbutton.grid(row=1, column=1)

mWindow.mainloop()


import os
import time
import tkinter as tk
import threading

from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox

windowMain = Tk()
windowMain.geometry("800x450")
windowMain.title("Projection Control")
windowMain.configure(background="black")


imgTitleBar = PhotoImage(file="images/titlebar.gif")
lblTitleBar = Label(windowMain, image=imgTitleBar)
lblTitleBar.pack(fill=tk.Y, side=tk.TOP)

def goPowerOn():
    os.system("functions/poweron000.py")

    frameProgressBar = ttk.Frame()
    #frameProgressBar
    #frameProgressBar.pack(expand = True, fill = BOTH)
    frameProgressBar.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

    frameProgressText = Text(frameProgressBar)
    frameProgressText.pack()
    frameProgressText.insert(END, "PROJECTOR IS WARMING UP - PLEASE WAIT")


    progressBar = Progressbar(frameProgressBar,orient=HORIZONTAL,length=100,mode='determinate')

    #progressBar.pack(expand = True, fill = BOTH)
    progressBar.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

    progressBar.start(650)

    frameProgressBar.after(65000, lambda: frameProgressBar.destroy())


def goPowerOff():
    os.system("functions/poweroff000.py")

    frameProgressBar = ttk.Frame()
    frameProgressBar.pack(expand = True, fill = BOTH)

    frameProgressText = Text(frameProgressBar)
    frameProgressText.pack()
    frameProgressText.insert(END, "PROJECTOR IS POWERING DOWN - PLEASE WAIT")

    progressBar = Progressbar(frameProgressBar,orient=HORIZONTAL,length=100,mode='determinate')

    progressBar.pack(expand = True, fill = BOTH)

    progressBar.start(1100)

    frameProgressBar.after(110000, lambda: frameProgressBar.destroy())

def goBlankOff():
    os.system("functions/blankscreenoff0.py")
    #blankTimeOut(0)

def blankTimeOut():
    os.system("functions/blankscreenon00.py")
    tmrBlankScreen = threading.Timer(5.0, lambda: showBlankTimeOutMsg())
    tmrBlankScreen.start()
    #messagebox.showinfo("Timeout Controller", "Blank Screen Timeout Reached!"

def showBlankTimeOutMsg():
    lblBlankTimeout = Label(windowMain, text="NOTICE: Blank Screen Disabled - Timeout Reached!")
    lblBlankTimeout.pack(fill=tk.X, pady=10)
    os.system("functions/blankScreenOff0.py")

def settingsWindow():
    windowSettings = Tk()
    windowSettings.geometry("600x350")
    windowSettings.title("Settings")
    windowSettings.configure(background="black")
    windowSettings.mainloop()

btnPowerOn = tk.Button(windowMain, command = goPowerOn, bg="#000000")
#btnPowerOn.pack()
imgPowerOn = PhotoImage(file="images/power_on.gif")
btnPowerOn.config(image=imgPowerOn)
# btnPowerOn.grid(row=0, column=0)
btnPowerOn.pack(padx=5, pady=10, side=tk.LEFT)

btnPowerOff = tk.Button(windowMain, command = goPowerOff)
#btnPowerOff.pack()
imgPowerOff = PhotoImage(file="images/power_off.gif")
btnPowerOff.config(image=imgPowerOff)
#btnPowerOff = Button(windowMain, text="Power Off", command = goPowerOff)
#btnPowerOff.grid(row=0, column=1)
btnPowerOff.pack(padx=5, pady=20, side=tk.LEFT)

btnBlankOn = tk.Button(windowMain, command = blankTimeOut)
#btnBlankOn.pack()
imgBlankOn = PhotoImage(file="images/blankscreen_on.gif")
btnBlankOn.config(image=imgBlankOn)
#btnBlankOn = Button(windowMain, text = "Blank Screen ON", command = goBlankOn)
# btnBlankOn.grid(row=1, column=0)
btnBlankOn.pack(padx=5, pady=20, side=tk.LEFT)

btnBlankOff = tk.Button(windowMain, command = goBlankOff)
#btnBlankOff.pack()
imgBlankOff = PhotoImage(file="images/blankscreen_off.gif")
btnBlankOff.config(image=imgBlankOff)
#btnBlankOff = Button(windowMain, text = "Blank Screen OFF", command = goBlankOff)
# btnBlankOff.grid(row=1, column=1)
btnBlankOff.pack(padx=5, pady=20, side=tk.LEFT)

#btnQuit = tk.Button(windowMain, text = "Quit", command=windowMain.destroy)
#btnQuit.grid(row=2, column=3)

#btnSettings = tk.Button(windowMain, text="Settings", command = settingsWindow)
#btnSettings.grid(row=2, column=2)

windowMain.mainloop()
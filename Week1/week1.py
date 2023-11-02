from tkinter import *
import tkinter.font as font
import subprocess

dialog = Tk()
dialog.title("Week 1")
dialog.geometry("350x350")


def signalbutton():
    subprocess.run(["python", "Week1\\signalfirst.py"], check=True)


def sin_cosbutton():
    subprocess.run(["python", "Week1\\sin_cos.py"], check=True)


buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

signal = Button(dialog, text="Task 1", width="13",
                height="3", command=signalbutton, font=buttonFont)

sin_cos = Button(dialog, text="Task 2", width="13",
                 height="3", command=sin_cosbutton, font=buttonFont)


signal.pack(pady=(0, 20))
sin_cos.pack(pady=(0, 20))
dialog.mainloop()


lst=['levels','bits']
var=IntVar()

for i in range(0,1):
    Radiobutton(dialog,value=i,variable=var,text=lst[i])
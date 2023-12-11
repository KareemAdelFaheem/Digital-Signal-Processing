from tkinter import *
import tkinter.font as font
import subprocess

dialog = Tk()
dialog.title("Week 2")
dialog.geometry("600x600")


def Fastconv():
    subprocess.run(["python", "Week7/Correlation.py"], check=True)


def Fastcorr():
    subprocess.run(["python", "Week7/Time_analysis.py"], check=True)


buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

convbutton = Button(dialog, text="FastConvolution", width="13",
                        height="3", command=Fastconv, font=buttonFont)

corrbutton = Button(dialog, text="FastCorrelation", width="13",
                          height="3", command=Fastcorr, font=buttonFont)


convbutton.pack(pady=(20, 20))
corrbutton.pack(pady=(0, 20))

dialog.mainloop()

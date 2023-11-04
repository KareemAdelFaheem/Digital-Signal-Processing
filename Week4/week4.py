from tkinter import *
import tkinter.font as font
import subprocess

dialog = Tk()
dialog.title("Week 4")
dialog.geometry("750x750")

def FourierTransform():
    subprocess.run(["python", "Week4\Fouriertransform.py"], check=True)




buttonFont = font.Font(family='Helvetica', size=10, weight='bold')
FourierButton = Button(dialog, text="Quantize", width="13",
                        height="3", command=FourierTransform, font=buttonFont)

FourierButton.pack(pady=(20,20))
dialog.mainloop()
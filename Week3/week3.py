from tkinter import *
import tkinter.font as font
import subprocess

dialog = Tk()
dialog.title("Week 3")
dialog.geometry("750x750")

def quanButton():
    subprocess.run(["python", "Week3\quantization.py"], check=True)

buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

quantizationButton = Button(dialog, text="Quantize", width="13",
                        height="3", command=quanButton, font=buttonFont)

quantizationButton.pack(pady=(20,20))
dialog.mainloop()
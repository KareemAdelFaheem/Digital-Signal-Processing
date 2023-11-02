from tkinter import *
import tkinter.font as font
import subprocess

dialog = Tk()
dialog.title("Week 2")
dialog.geometry("600x600")

def addbutton():
    subprocess.run(["python", "Week2/addition.py"], check=True)
    
def subbutton():
    subprocess.run(["python", "Week2/subtraction.py"], check=True)

def multbutton():
    subprocess.run(["python", "Week2/multiplication.py"], check=True)
    
def squarebutton():
    subprocess.run(["python", "Week2/squaring.py"], check=True)
    
def shiftbutton():
    subprocess.run(["python", "Week2/shifting.py"], check=True)
    
def normbutton():
    subprocess.run(["python", "Week2/normalization.py"], check=True)
    
def accbutton():
    subprocess.run(["python", "Week2/accumulation.py"], check=True)


buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

additionbutton = Button(dialog, text="Addition", width="13",
                        height="3", command=addbutton, font=buttonFont)

subtractionbutton = Button(dialog, text="Subtraction", width="13",
                           height="3", command=subbutton, font=buttonFont)

multiplicationbutton = Button(dialog, text="Multiplication", width="13",
                              height="3", command=multbutton, font=buttonFont)

squaringbutton = Button(dialog, text="Squaring", width="13",
                              height="3", command=squarebutton, font=buttonFont)

shiftingbutton = Button(dialog, text="Shifting", width="13",
                              height="3", command=shiftbutton, font=buttonFont)

normalizationbutton = Button(dialog, text="Normalization", width="13",
                              height="3", command=normbutton, font=buttonFont)

accumulationbutton = Button(dialog, text="Accumulation", width="13",
                              height="3", command=accbutton, font=buttonFont)


additionbutton.pack(pady=(20,20))
subtractionbutton.pack(pady=(0,20))
multiplicationbutton.pack(pady=(0,20))
squaringbutton.pack(pady=(0,20))
shiftingbutton.pack(pady=(0,20))
normalizationbutton.pack(pady=(0,20))
accumulationbutton.pack(pady=(0,20))

dialog.mainloop()
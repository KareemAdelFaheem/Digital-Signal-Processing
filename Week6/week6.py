from tkinter import *
import tkinter.font as font
import subprocess

dialog = Tk()
dialog.title("Week 2")
dialog.geometry("600x600")

def Smoothing():
    subprocess.run(["python", "Week6/Smoothing.py"], check=True)
    
def Sharpening():
    subprocess.run(["python", "Week6/Sharpening.py"], check=True)

def DelayingOrAdvancing():
    subprocess.run(["python", "Week6/DelayingorAdvancing.py"], check=True)
    
def Floding():
    subprocess.run(["python", "Week2/squaring.py"], check=True)
    
def DorAfloded():
    subprocess.run(["python", "Week2/shifting.py"], check=True)
    
def DC():
    subprocess.run(["python", "Week2/normalization.py"], check=True)
    
def Convolution():
    subprocess.run(["python", "Week2/accumulation.py"], check=True)


buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

smottingbutton = Button(dialog, text="Smoothing", width="13",
                        height="3", command=Smoothing, font=buttonFont)

Sharpeningbutton = Button(dialog, text="Sharpening", width="13",
                           height="3", command=Sharpening, font=buttonFont)

DelayorAdvancebutton = Button(dialog, text="Delay&Advance", width="13",
                              height="3", command=DelayingOrAdvancing, font=buttonFont)

Flodingbutton = Button(dialog, text="Folding", width="13",
                              height="3", command=Floding, font=buttonFont)

DelayorAdvancefoldedbutton = Button(dialog, text="Delay&AdvanceFolded", width="13",
                              height="3", command=DorAfloded, font=buttonFont)

DCbutton = Button(dialog, text="DC Component", width="13",
                              height="3", command=DC, font=buttonFont)

Convolutionbutton = Button(dialog, text="Convolution", width="13",
                              height="3", command=Convolution, font=buttonFont)


smottingbutton.pack(pady=(20,20))
Sharpeningbutton.pack(pady=(0,20))
DelayorAdvancebutton.pack(pady=(0,20))
Flodingbutton.pack(pady=(0,20))
DelayorAdvancefoldedbutton.pack(pady=(0,20))
DCbutton.pack(pady=(0,20))
Convolutionbutton.pack(pady=(0,20))

dialog.mainloop()
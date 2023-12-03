from tkinter import *
from tkinter import filedialog
import CompareSignal as tst
import numpy as np


dialog = Tk()
dialog.title("Time Analysis")
dialog.geometry("400x400")


def Correlation():
    xsignal1 = []
    xsignal2 = []
    ysignal1 = []
    ysignal2 = []
    correlationsignal = []
    TimeDelay=0

    signal1 = filedialog.askopenfilename(
        initialdir="A:/Programming/Python dsp tasks/Final Task/Signals/InputSignals", title="Which Signal")

    signal2 = filedialog.askopenfilename(
        initialdir="A:/Programming/Python dsp tasks/Final Task/Signals/InputSignals", title="Which Signal")

    with open(signal1, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            xsignal1.append(int(parts[0]))
            ysignal1.append(float(parts[1]))

    with open(signal2, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            xsignal2.append(int(parts[0]))
            ysignal2.append(float(parts[1]))

    N = len(ysignal1)

    for j in range(0, N):
        value = 0
        for n in range(0, N):
            d = n+j
            if (n+j) >= N:
                d -= N
            value += ysignal1[n]*ysignal2[d]
        correlationsignal.append(value/N)

    maxindex = 0
    maxvalue = 0
    for i in correlationsignal:
        if i >= maxvalue:
            maxvalue = i

    maxindex = correlationsignal.index(maxvalue)
    TimeDelay=maxindex/int(Fs.get("1.0",END))
    print(TimeDelay)


Corrbutton = Button(dialog, width=17, height=4,
                    text="Time delay", command=Correlation)
f = Frame(dialog)
lbl = LabelFrame(f, text="Enter Sampling frequency")
Fs = Text(lbl, width=50, height=2)

f.pack(pady=10)
Fs.pack()
lbl.pack()
Corrbutton.pack(pady=50)
dialog.mainloop()

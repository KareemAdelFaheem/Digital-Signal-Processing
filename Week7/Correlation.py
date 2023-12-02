from tkinter import *
from tkinter import filedialog
import CompareSignal as tst
import numpy as np


dialog = Tk()
dialog.title("Correlation")
dialog.geometry("400x400")

correlationsignal = []
xsignal1 = []


def Correlation():
    global xsignal1
    xsignal2 = []
    ysignal1 = []
    ysignal2 = []
    r = []
    global correlationsignal

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
        r.append(value/N)

    denominator = 0
    y1square = 0
    y2square = 0
    for j in range(0, N):
        y1square += np.power(ysignal1[j], 2)
        y2square += np.power(ysignal2[j], 2)

    denominator = (np.sqrt(y1square*y2square))/N

    for i in r:
        correlationsignal.append(i/denominator)


def compare():
    print(correlationsignal)
    tst.Compare_Signals("Signals/Outputsignals/CorrOutput.txt",
                        xsignal1, correlationsignal)


Corrbutton = Button(dialog, width=17, height=4,
                    text="Correlation", command=Correlation)
compbutton = Button(dialog, width=17, height=4,
                    text="Compare", command=compare)
Corrbutton.pack(pady=50)
compbutton.pack()
dialog.mainloop()

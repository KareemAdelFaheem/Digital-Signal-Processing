from tkinter import *
from tkinter import filedialog
dialog = Tk()
dialog.geometry("250x250")
dialog.title("Convolution")


def Sharpening():
    xsignal1 = []
    xsignal2 = []
    ysignal1 = []
    ysignal2 = []
    convsignal = []

    signal1 = filedialog.askopenfilename(
        initialdir="A:\Programming\Python dsp tasks\Final Task\Signals\InputSignals", title="Which Signal")

    signal2 = filedialog.askopenfilename(   
        initialdir="A:\Programming\Python dsp tasks\Final Task\Signals\InputSignals", title="Which Signal")

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

    min = xsignal1[0]+xsignal2[0]
    max = xsignal1[len(xsignal1)-1]+xsignal2[len(xsignal2)-1]

    for k in range(min, max):
        for n in range(min, max):
            convsignal.append(ysignal1[k]*ysignal2[xsignal2.index(n-k)])

    print(convsignal)


btn = Button(dialog, text="Sharpen", width=20, height=4, command=Sharpening)


btn.pack(pady=40)
dialog.mainloop()

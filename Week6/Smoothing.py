from tkinter import *
from tkinter import filedialog
dialog = Tk()
dialog.geometry("250x250")
dialog.title("Smoothing")


def Smoothing():
    ysignal = []
    smoothedsignal = []

    signal = filedialog.askopenfilename(
        initialdir="A:\Programming\Python dsp tasks\Final Task\Signals\InputSignals", title="Which Signal")

    with open(signal, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            ysignal.append(float(parts[1]))
    print(ysignal)
    SmoothWidth = int(Nofstrides.get("1.0", END))
    for i in range(len(ysignal)-SmoothWidth+1):
        Smoothedvalue = 0
        for j in range(i, i+SmoothWidth):
            Smoothedvalue += ysignal[j]

        smoothedsignal.append(Smoothedvalue/SmoothWidth)

    print(smoothedsignal)


frm = Frame(dialog)
txtLabel = LabelFrame(frm, text="Enter number of Strides")
Nofstrides = Text(txtLabel, width=50, height=2)
btn = Button(dialog, text="Smooth", width=20, height=4, command=Smoothing)

frm.pack()
txtLabel.pack()
Nofstrides.pack()
btn.pack(pady=40)
dialog.mainloop()


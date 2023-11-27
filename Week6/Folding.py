from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt



dialog = Tk()
dialog.geometry("400x400")
dialog.title("Folding")


def Folding():
    xsignal=[]
    ysignal = []
    FoldedSignal=[]

    signal = filedialog.askopenfilename(
        initialdir="A:\Programming\Python dsp tasks\Final Task\Signals\InputSignals", title="Which Signal")

    with open(signal, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            xsignal.append(float(parts[0]))
            ysignal.append(float(parts[1]))

    for i in range(len(ysignal)):

        FoldedSignal.append(ysignal[-1-i])
    
    figure, add = plt.subplots(2, 1, figsize=(6, 8))

    add[0].plot(xsignal , ysignal)
    add[0].set_title("Original Signal")
    add[1].plot(FoldedSignal, ysignal)
    add[1].set_title("Folded Signal")

    plt.show()
    print(FoldedSignal)

    



Foldingbtn = Button(dialog, text="Fold", width=20, height=4, command=Folding)


Foldingbtn.pack(pady=40)
dialog.mainloop()


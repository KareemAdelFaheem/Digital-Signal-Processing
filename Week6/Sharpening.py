from tkinter import *
from tkinter import filedialog
dialog = Tk()
dialog.geometry("250x250")
dialog.title("Sharpening")


def Sharpening():
    ysignal = []
    Firstderivative=[]
    SecondDerivative=[]

    signal = filedialog.askopenfilename(
        initialdir="A:\Programming\Python dsp tasks\Final Task\Signals\InputSignals", title="Which Signal")

    with open(signal, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            ysignal.append(float(parts[1]))
    
    for i in range(1,len(ysignal)):
        Firstderivative.append(ysignal[i]-ysignal[i-1])
        if(i!=(len(ysignal)-1)):
            SecondDerivative.append(ysignal[i+1]-2*ysignal[i]+ysignal[i-1])
    
    print(Firstderivative)
    print(SecondDerivative)
    
    



btn = Button(dialog, text="Sharpen", width=20, height=4, command=Sharpening)


btn.pack(pady=40)
dialog.mainloop()



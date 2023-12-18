from tkinter import *
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import utils as ut
import comparesignal2 as tst

root = Tk()
root.title("Filtering")
root.geometry("500x500")

w = []
h = []
N = 0
signal = []

def Window_Method():
    global N
    N = 0
    N = int(N)
    w.clear()

    attenutation = int(stopbandtxt.get(1.0, "end"))
    transition = int(transitiontxt.get(1.0, "end"))
    samplingfreq = int(samplingfrequencytxt.get(1.0, "end"))

    if (attenutation <= 21):
        N = np.ceil((samplingfreq*0.9)/transition)
        if (N % 2 == 0):
            N += 1

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            w.append(1)

    elif (attenutation <= 44):
        N = np.ceil((samplingfreq*3.1)/transition)
        if (N % 2 == 0):
            N += 1

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            w.append(0.5 + (0.5 * np.cos((2 * np.pi * i) / N)))

    elif (attenutation <= 53):
        N = np.ceil((samplingfreq * 3.3) / transition)
        if (N % 2 == 0):
            N += 1

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            w.append(0.54 + (0.46 * np.cos((2 * np.pi * i) / N)))

    elif (attenutation <= 74):
        N = np.ceil((samplingfreq * 5.5) / transition)
        if (N % 2 == 0):
            N += 1

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            w.append(0.42 + (0.5 * np.cos((2 * np.pi * i) / (N - 1))) +
                     (0.08 * np.cos((4 * np.pi * i) / (N - 1))))

    return w


def Filter_Type():
    global N
    N = int(N)
    h.clear()

    transition = int(transitiontxt.get(1.0, "end"))
    samplingfreq = int(samplingfrequencytxt.get(1.0, "end"))
    filtertype = int(Filtertypetxt.get(1.0, "end"))
    f1 = int(F1txt.get(1.0, "end"))
    f2 = int(F2txt.get(1.0, "end"))
    Fc1 = 0
    Fc2 = 0

    if (filtertype == 0): # Low Pass Filter
        Fc1 = (f1+(transition/2))/samplingfreq
        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            if (i == 0):
                h.append(2 * Fc1)
                continue

            h.append(2 * Fc1 * ((np.sin(i * (2 * np.pi * Fc1))) / (i * (2 * np.pi * Fc1))))

    elif (filtertype == 1): # High Pass Filter
        Fc1 = (f1-(transition/2))/samplingfreq
        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            if (i == 0):
                h.append(1 - (2 * Fc1))
                continue
            h.append(-2 * Fc1 * (np.sin(i * (2 * np.pi * Fc1)) / (i * (2 * np.pi * Fc1))))

    elif (filtertype == 2): # Band Pass Filter
        Fc1 = (f1-(transition/2))/samplingfreq
        Fc2 = (f2+(transition/2))/samplingfreq

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            if (i == 0):
                h.append(2 * (Fc2 - Fc1))
                continue

            h.append((2 * Fc2 * (np.sin(i * (2 * np.pi * Fc2)) / (i * (2 * np.pi * Fc2)))) -
                     (2 * Fc1 * (np.sin(i * (2 * np.pi * Fc1)) / (i * (2 * np.pi * Fc1)))))

    elif (filtertype == 3): # Band Reject Filter
        Fc1 = (f1+(transition/2))/samplingfreq
        Fc2 = (f2-(transition/2))/samplingfreq

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            if (i == 0):
                h.append(1 - (2 * (Fc2 - Fc1)))
                continue

            h.append((2 * Fc1 * (np.sin(i * (2 * np.pi * Fc1)) / (i * (2 * np.pi * Fc1)))) -
                     (2 * Fc2 * (np.sin(i * (2 * np.pi * Fc2)) / (i * (2 * np.pi * Fc2)))))

    return h


def Filtering():
    w = Window_Method()
    h = Filter_Type()
    result = ut.multiply(w, h)
    # print(result)
    plot(h, result)
    tst.SignalSamplesAreEqual("Signals/Project signal/Testcase1/LPFCoefficients.txt",result)
    tst.SignalSamplesAreEqual("Signals/Project signal/Testcase3/HPFCoefficients.txt",result)
    tst.SignalSamplesAreEqual("Signals/Project signal/Testcase5/BPFCoefficients.txt",result)
    tst.SignalSamplesAreEqual("Signals/Project signal/Testcase7/BSFCoefficients.txt",result)


def Filtering_Uploaded_Signal():
    ySignal = []
    signalresult = []
    result = []

    ySignal.clear()
    result.clear()
    signalresult.clear()

    signal = filedialog.askopenfilename(
        initialdir="Project_Files/Practical task 1/FIR test cases", title="Which Signal")

    with open(signal, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            ySignal.append(int(parts[1]))

    w = Window_Method()
    h = Filter_Type()
    result = ut.multiply(w, h)
    signalresult = ut.fast_convolution(result, ySignal)
    print(signalresult)
    plot(ySignal, signalresult)

    tst.SignalSamplesAreEqual("Signals/Project signal/Testcase2/ecg_low_pass_filtered.txt",signalresult)
    tst.SignalSamplesAreEqual("Signals/Project signal/Testcase4/ecg_high_pass_filtered.txt",signalresult)
    tst.SignalSamplesAreEqual("Signals/Project signal/Testcase6/ecg_band_pass_filtered.txt",signalresult)
    tst.SignalSamplesAreEqual("Signals/Project signal/Testcase8/ecg_band_stop_filtered.txt",signalresult)

def plot(orginal, filtered):
    fig, fir = plt.subplots(2, 1, figsize=(6, 8))
    fir[0].plot(orginal)
    fir[0].set_title("Original Signal")
    fir[1].plot(filtered)
    fir[1].set_title("Filtered Signal")
    plt.show()

frame = Frame(root)

lbl = Label(root, text="Low Pass: 0, High Pass: 1, Band Pass: 2, Band Reject: 3")
Filtertypelbl = LabelFrame(frame, text="Filter Type")
Filtertypetxt = Text(Filtertypelbl, width=50, height=2)
Samplingfreqlbl = LabelFrame(frame, text="Sampling Frequency")
samplingfrequencytxt = Text(Samplingfreqlbl, width=50, height=2)
transitionlbl = LabelFrame(frame, text="Transition Band")
transitiontxt = Text(transitionlbl, width=50, height=2)
stopbandlbl = LabelFrame(frame, text="Stop Band Attenuation")
stopbandtxt = Text(stopbandlbl, width=50, height=2)
F1lbl = LabelFrame(frame, text="F1")
F1txt = Text(F1lbl, width=50, height=2)
F2lbl = LabelFrame(frame, text="F2")
F2txt = Text(F2lbl, width=50, height=2)


Filterbutton = Button(frame, width="17", height="3", text="Filter", command=Filtering)

uploadbutton = Button(frame, width="17", height="3", text="Upload Signal", command=Filtering_Uploaded_Signal)

lbl.pack()
frame.pack()
Filtertypelbl.pack()
Filtertypetxt.pack()
Samplingfreqlbl.pack()
samplingfrequencytxt.pack()
transitionlbl.pack()
transitiontxt.pack()
stopbandlbl.pack()
stopbandtxt.pack()
F1lbl.pack()
F1txt.pack()
F2lbl.pack()
F2txt.pack()

Filterbutton.pack()
uploadbutton.pack()
root.mainloop()

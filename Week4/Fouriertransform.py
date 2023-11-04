from tkinter import *
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import signalcompare as tst

root = Tk()
root.title("Week 4")
root.geometry("500x400")

def Fourier_transform():
    xValues = []
    yValues = []
    xOfn = []
    xOfk = []
    amplitude = []
    phase = []
    sigma = []

    signal = filedialog.askopenfilename(
        initialdir="Lab 4/Test Cases",
        title="Which Signal ?",
    )
    chk = int(np.loadtxt(signal, skiprows = 1, max_rows = 1))

    with open(signal, "r") as f:
        for i in range(3): 
            next(f)

        for line in f:
            parts = line.strip().split()
            xValues.append(float(parts[0]))
            yValues.append(float(parts[1]))

    N = len(yValues)
    
    if (chk == 0):
        xOfn = yValues
        j = 1j

        for k in range (0, N):
            harmonic_value = 0
            for n in range (0, N):
                harmonic_value += xOfn[n] * np.exp((-j * 2 * np.pi * k * n) / N)
            xOfk.append(harmonic_value)
            amplitude.append(np.sqrt(np.power(np.real(harmonic_value), 2) + np.power(np.imag(harmonic_value), 2)))
            phase.append(np.arctan(float(np.imag(harmonic_value) / np.real(harmonic_value))))

        fund_freq = 0
        fs = int(freq.get(1.0, "end"))

        for i in range(0, len(amplitude)):
            fund_freq += (2 * np.pi * fs) / N
            sigma.append(fund_freq)

        # if(tst.SignalComapreAmplitude(yValues,amplitude) and tst.SignalComaprePhaseShift(yValues,phase)):
        #     print ("Success")
        
        modWindow = Toplevel(root)
        modWindow.title("Modification")
        modWindow.geometry("500x400")
        frame = Frame(modWindow)
        lf1 = LabelFrame(frame, text="Modify Amplitude")
        lf2 = LabelFrame(frame, text="Modify Phase Shift")
        amp_mod = Text(lf1, width=20, height=2)
        phase_mod = Text(lf2, width=20, height=2)
        # update = Button(frame, text="Update", width="12", height="2", font="30", bg="white", fg="black", command=)
        frame.pack()
        lf1.pack()
        lf2.pack()
        amp_mod.pack()
        phase_mod.pack()
        # update.pack()
        figure, DFT = plt.subplots(2, 1, figsize=(6, 8))
        DFT[0].bar(sigma, amplitude)
        DFT[0].set_title("Frequency / Amplitude")
        DFT[1].bar(sigma, phase)
        DFT[1].set_title("Frequency / Phase")

    else:
        real = []
        img = []
        j = 1j
        
        for i in range(N):
            real.append(xValues[i] * np.cos(yValues[i]))
            img.append(xValues[i] * np.sin(yValues[i]))
            xOfk.append(real[i] + img[i] * j)

        for n in range (0, N):
            harmonic_value = 0
            for k in range (0, N):
                harmonic_value += (1 / N) * xOfk[k] * np.exp((j * 2 * np.pi * n * k) / N)
            xOfn.append(harmonic_value)

        # output = np.loadtxt("Lab 4\Test Cases\IDFT\Output_Signal_IDFT.txt", skiprows=3, delimiter=' ')
        # tst_output = output[:, 1]
        # if tst.SignalComapreAmplitude(xOfn, tst_output):
        #     print("Success")

        plt.plot(xOfn)
        plt.xlabel("time")
        plt.ylabel("amplitude")
        plt.title("IDFT")
    plt.show()

freq_label = Label(root, text="Enter the Sampling Frequency in HZ", pady=40)
freq = Text(root, width=20, height=2)
upload = Button(root, text="Upload", width=12, height=2, command=Fourier_transform)

freq_label.pack()
freq.pack()
upload.pack()
root.mainloop()

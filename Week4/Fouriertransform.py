from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt


dialog = Tk()
dialog.title("Week 4")
dialog.geometry("500x400")


def Fouriertransform():
    x_value = []
    xof_n = []
    xof_k = []
    amplitude = []
    phase = []
    segma_fundfreq = []

    signal1 = filedialog.askopenfilename(
        initialdir="Lab 2/input",
        title="Signal 1",
    )
    file_label.config(text=f"Selected File: {signal1}")

    with open(signal1, "r") as f:
        for i in range(3):
            next(f)

        for line in f:
            parts = line.strip().split()
            x_value.append(float(parts[0]))
            xof_n.append(float(parts[1]))

    N = len(xof_n)
    j = 1j

    for k in range(0, N):
        harmonic_value = 0
        for n in range(0, N):
            harmonic_value += xof_n[n]*np.exp((-j*2*np.pi*k*n)/N)
            # xof_k.append(xof_n[n]*np.exp((-j*2*np.pi*k*n)/N))
        xof_k.append(harmonic_value)
        amplitude.append(np.sqrt(
            np.power(np.real(harmonic_value), 2)+np.power(np.imag(harmonic_value), 2)))
        phase.append(
            np.arctan(np.imag(harmonic_value)/np.real(harmonic_value)))

    Fs = int(freqtxt.get("1.0", END))
    fundamentalfreq = 0

    for i in range(0, len(amplitude)):
        fundamentalfreq += (2*np.pi*Fs)/N
        segma_fundfreq.append(fundamentalfreq)

    figure, add = plt.subplots(2, 1, figsize=(6, 8))

    add[0].plot(segma_fundfreq, amplitude)
    add[0].set_title("Frequency/Amplitude")
    add[1].plot(segma_fundfreq, phase)
    add[1].set_title("Frequency/Phase")
    plt.show()
    print(xof_k)
    print(amplitude)
    print(phase)


file_label = tk.Label(dialog, text="Selected File: ", pady=40)
uploadbtn = Button(dialog, text="Upload", width=12,
                   height=2, command=Fouriertransform)
textfield_label = tk.Label(
    dialog, text="Enter the Sampling Frequency in HZ", pady=40)
freqtxt = Text(dialog, width=20, height=2)


textfield_label.pack()
freqtxt.pack()
file_label.pack()
uploadbtn.pack()

dialog.mainloop()

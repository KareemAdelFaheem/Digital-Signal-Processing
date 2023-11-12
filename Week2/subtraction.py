from tkinter import *
from tkinter import filedialog
import tkinter.font as font
import tkinter as tk
import matplotlib.pyplot as plt
from comparesignals import SignalSamplesAreEqual


root = tk.Tk()
root.title("Subtraction")
root.geometry("400x400")


def subtraction():
    x_value = []
    y1_value = []
    y2_value = []
    newy_value = []

    signal1 = filedialog.askopenfilename(
        initialdir="Lab 2/input",
        title="Which signal?",
    )
    signal2 = filedialog.askopenfilename(
        initialdir="Lab 2/input",
        title="Which signal?",
    )

    file_label.config(text=f"Selected File: {signal1}")
    file_label2.config(text=f"Selected File: {signal2}")

    with open(signal1, "r") as f:
        for _ in range(3):
            next(f)

        for line in f:
            parts = line.strip().split()
            x_value.append(float(parts[0]))
            y1_value.append(float(parts[1]))

    with open(signal2, "r") as f:
        for _ in range(3):
            next(f)

        for line in f:
            parts = line.strip().split()
            y2_value.append(float(parts[1]))

    for i in range(0, len(y1_value)):
        newy_value.append(y2_value[i] - y1_value[i])

    # test signal1 - signal2
    SignalSamplesAreEqual(
        "Signals\Outputsignals\signal1-signal2.txt", x_value, newy_value)

    # test signal1 - signal3
    SignalSamplesAreEqual(
        "Signals\Outputsignals\signal1-signal3.txt", x_value, newy_value)

    fig, sub = plt.subplots(3, 1, figsize=(6, 8))

    sub[0].plot(x_value, y1_value)
    sub[0].set_title("Signal 1")
    sub[1].plot(x_value, y2_value)
    sub[1].set_title("Signal 2")
    sub[2].plot(x_value, newy_value)
    sub[2].set_title("Subtracted signal")

    plt.show()


file_label = tk.Label(root, text="Selected File: ", pady=40)
file_label2 = tk.Label(root, text="Selected File: ", pady=40)

sub = Button(
    root,
    text="Upload",
    width="12",
    height="2",
    font="30",
    bg="white",
    fg="black",
    command=subtraction,
)
file_label.pack()
file_label2.pack()
sub.pack()
root.mainloop()

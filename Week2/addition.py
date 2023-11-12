from tkinter import *
from tkinter import filedialog
import tkinter as tk
import matplotlib.pyplot as plt
from comparesignals import SignalSamplesAreEqual


root = tk.Tk()
root.title("Addition")
root.geometry("500x500")


def addition():
    x_value = []
    y1_value = []
    y2_value = []
    y3_value = []
    newy_value = []

    signal1 = filedialog.askopenfilename(
        initialdir="Lab 2/input",
        title="Signal 1",
    )
    signal2 = filedialog.askopenfilename(
        initialdir="Lab 2/input",
        title="Signal 2",
    )

    file_label.config(text=f"Selected File: {signal1}")
    file_label2.config(text=f"Selected File: {signal2}")

    with open(signal1, "r") as f:
        for i in range(3):
            next(f)

        for line in f:
            parts = line.strip().split()
            x_value.append(float(parts[0]))
            y1_value.append(float(parts[1]))

    with open(signal2, "r") as f:
        for i in range(3):
            next(f)

        for line in f:
            parts = line.strip().split()
            y2_value.append(float(parts[1]))

    for i in range(0, len(y1_value)):
        newy_value.append(y1_value[i] + y2_value[i])

    SignalSamplesAreEqual(
        "Signals\Outputsignals\Signal1+signal2.txt", x_value, newy_value)
    SignalSamplesAreEqual(
        "Signals\Outputsignals\signal1+signal3.txt", x_value, newy_value)

    figure, add = plt.subplots(3, 1, figsize=(6, 8))

    add[0].plot(x_value, y1_value)
    add[0].set_title("Signal 1")
    add[1].plot(x_value, y2_value)
    add[1].set_title("Signal 2")
    add[2].plot(x_value, newy_value)
    add[2].set_title("New signal")

    plt.show()


file_label = tk.Label(root, text="Selected File: ", pady=40)
file_label2 = tk.Label(root, text="Selected File: ", pady=40)

button = Button(
    root,
    text="Upload",
    width="12",
    height="2",
    font="30",
    bg="white",
    fg="black",
    command=addition,
)
file_label.pack()
file_label2.pack()
button.pack()
root.mainloop()

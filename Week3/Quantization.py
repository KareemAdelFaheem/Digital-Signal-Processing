from tkinter import *
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
# import QuanTest1 as t1
# import QuanTest2 as t2

root = Tk()
root.title("Signal Quantization")

def quantize_signal():
    xSignal = []
    ySignal = []
    y_index = []
    mid_points = []
    y_quantized = []
    encoded_x = []
    error = []
    interval_index=[]
    levels_or_bits = var.get()
    
    signal = filedialog.askopenfilename(
    initialdir="Lab 3",
    title="Which Signal ?",
    )

    with open(signal, "r") as f:
        for i in range(3):
            next(f)

        for line in f:
            parts = line.strip().split()
            xSignal.append(float(parts[0]))
            ySignal.append(float(parts[1]))

    if (levels_or_bits == 'levels'):
        levels = float(lvls.get(1.0, "end"))   
        
    elif (levels_or_bits == 'bits'):
        bits = int(bts.get(1.0, "end"))
        levels = np.power(2, bits)

    delta = (max(ySignal) - min(ySignal)) / levels

    x = min(ySignal)
    y_index.append(x)
    for i in range (int(levels)):
        x += delta
        y_index.append(round(x, 2))

    for i in range(len(y_index) - 1):
        mid_points.append((y_index[i] + y_index[i + 1]) / 2)

    for i in range(len(ySignal)):
        for j in range(len(y_index) - 1):
            if (ySignal[i] >= y_index[j] and ySignal[i] <= y_index[j + 1]):
                y_quantized.append((mid_points[j]))
                break

    for i in range(len(y_quantized)):
        encoded_x.append(format(mid_points.index(y_quantized[i]), '03b'))

    if (levels_or_bits == 'levels'):   
        for i in range(len(y_quantized)):
            interval_index.append(mid_points.index(y_quantized[i]) + 1)
        for i in range(len(ySignal)):
            error.append(round((y_quantized[i] - ySignal[i]), 3))

        print("Interval Index : ")
        for i in interval_index:
            print(i)

        print("\n")

        print("Encoded : ")
        for i in encoded_x:
            print(i)
            
        print("\n")

        print("Quantized : ")
        for i in y_quantized:
            print(round(i, 3))

        print("\n")

        print("Error : ")
        for i in y_quantized:
            print(round(i, 3))
        
    elif (levels_or_bits == 'bits'):
        print("Encoded : ")
        for i in encoded_x:
            print(i)
            
        print("\n")

        print("Quantized : ")
        for i in y_quantized:
            print(round(i, 3))

        print("\n")

    # t1.QuantizationTest1("Lab 3/Test 1/Quan1_Out.txt", encoded_x, y_quantized)
    # t2.QuantizationTest2("Lab 3/Test 2/Quan2_Out.txt", encoded_x, y_quantized)

    # fig, quan = plt.subplots(2, 1, figsize=(6, 8))
    
    # quan[0].plot(xSignal, ySignal)
    # quan[0].set_title('Original signal')
    # quan[1].plot(encoded_x, y_quantized)
    # quan[1].set_title('Quantized signal')
    # plt.show()


frame = Frame(root)
lf1 = LabelFrame(frame, text="Number of levels")
lf2 = LabelFrame(frame, text="Number of bits")
var = StringVar()
lorb1 = Radiobutton(frame, width="50", height="2", text="levels", value="levels", variable=var)
lorb2 = Radiobutton(frame, width="50", height="2", text="bits", value="bits", variable=var)
lvls = Text(lf1, width="50", height="2")
bts = Text(lf2, width="50", height="2")
button = Button(
    frame,
    text="Upload",
    width="12",
    height="2",
    font="30",
    bg="white",
    fg="black",
    command=quantize_signal,
)

frame.pack()
lf1.pack()
lf2.pack()
lorb1.pack()
lorb2.pack()
lvls.pack()
bts.pack()
button.pack()
root.mainloop()
from tkinter import *
from tkinter import filedialog
import numpy as np
import utils as ut

root = Tk()
root.title("Resampling")
root.geometry("500x500")
upsampled=[]
def upsampling(ysignal,m,l):
    global upsampled
    upsamplingfactor=l
    downsamplingfactor=m
    upsampled=ysignal
    for i in range(0,upsamplingfactor*len(ysignal)-upsamplingfactor,upsamplingfactor):
        for j in range(0,upsamplingfactor-1):
            upsampled.insert(i+1,0)
       
    return 0
def downsampling(signal,m,l):
    return 0
def both(signal,m,l):
    return 0

def Resampling():
    M=int(Mtxt.get("1.0",END))
    L=int(Ltxt.get("1.0",END))
    ySignal=[]
    signal = filedialog.askopenfilename(
        initialdir="Lab 8/Fast Convolution", title="Which Signal")
    with open(signal, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            ySignal.append(int(parts[1]))

    if(M==0 and L!=0):
        upsampling(ySignal,M,L)
    if(M!=0 and L==0):
        downsampling(ySignal,M,L)
    if(M!=0 and L!=0):
        both(ySignal,M,L)
    if(M==0 and L==0):
        print("Error in M & L")


w = []
h = []
N = 0
signal = []


def Widnowmethod():
    global N
    N = int(N)
    attenutation = int(stopbandtxt.get("1.0", END))
    transition = int(transitiontxt.get("1.0", END))
    samplingfreq = int(samplingfrequencytxt.get("1.0", END))

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
            w.append(0.5+(0.5*np.cos((2*np.pi*i)/N)))

    elif (attenutation <= 53):
        N = np.ceil((samplingfreq*3.3)/transition)
        if (N % 2 == 0):
            N += 1
        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            w.append(0.54+(0.46*np.cos((2*np.pi*i)/N)))

    elif (attenutation <= 74):
        N = np.ceil((samplingfreq*5.5)/transition)
        if (N % 2 == 0):
            N += 1
        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            w.append(0.42+(0.5*np.cos((2*np.pi*i)/(N-1))) +
                     (0.08*np.cos((4*np.pi*i)/(N-1))))

    return w


def Filterpasstype():
    global N
    N = int(N)
    transition = int(transitiontxt.get("1.0", END))
    samplingfreq = int(samplingfrequencytxt.get("1.0", END))
    f1 = int(Ftxt.get("1.0", END))
    Fc1 = 0
    Fc2 = 0

    
    Fc1 = (f1+(transition/2))/samplingfreq
    for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
        if (i == ((N-1)/2)):
            h.append(2*Fc1)
            continue

        h.append(2*Fc1*(np.sin(i*(2*np.pi*Fc1)) / i*(2*np.pi*Fc1)))


    return h


def Filtering():
    global upsampled
    w = Widnowmethod()
    h = Filterpasstype()
    result = ut.fast_convolution(w, h)
    # print(result)
    print(upsampled)
    finalresult=ut.fast_convolution(result, upsampled)
    # print(finalresult)
    return finalresult


    

frame = Frame(root)
Mlbl = LabelFrame(frame, text="M")
Mtxt = Text(Mlbl, width=50, height=2)
Llbl = LabelFrame(frame, text="L")
Ltxt = Text(Llbl, width=50, height=2)
Flbl = LabelFrame(frame, text="F")
Ftxt = Text(Flbl, width=50, height=2)
transitionlbl = LabelFrame(frame, text="Transition width")
transitiontxt = Text(transitionlbl, width=50, height=2)
stopbandlbl = LabelFrame(frame, text="StopBand attenuation")
stopbandtxt = Text(stopbandlbl, width=50, height=2)
Samplingfreqlbl = LabelFrame(frame, text="Sampling frequency")
samplingfrequencytxt = Text(Samplingfreqlbl, width=50, height=2)



uploadbutton = Button(frame, width="17", height="3",
                      text="Upload",command=Resampling)
Filterbutton = Button(frame, width="17", height="3",
                      text="Filter",command=Filtering)

frame.pack()
Mlbl.pack()
Mtxt.pack()
Llbl.pack()
Ltxt.pack()
Flbl.pack()
Ftxt.pack()
transitionlbl.pack()
transitiontxt.pack()
stopbandlbl.pack()
stopbandtxt.pack()
Samplingfreqlbl.pack()
samplingfrequencytxt.pack()
uploadbutton.pack()
Filterbutton.pack(

)
root.mainloop()

import numpy as np

def multiply(w, h):
    multiplied_signal = []

    N = len(w)

    # Multiplication
    for i in range(N):
        multiplied_signal.append(w[i] * h[i])

    return multiplied_signal


def fast_convolution(ySignal1, ySignal2):
    xOfk1 = []
    xOfk2 = []
    yOfk = []
    convsignal = []

    N1 = len(ySignal1)
    N2 = len(ySignal2)
    new_len = N1 + N2 - 1

    for i in range(new_len - len(ySignal1)):
        ySignal1.append(0)
    for i in range(new_len - len(ySignal2)):
        ySignal2.append(0)

    j = 1j

    # DFT
    for k in range(0, new_len):
        harmonic_value = 0
        for n in range(0, new_len):
            harmonic_value += (ySignal1[n] * np.exp((-j * 2 * np.pi * k * n) / new_len))
        xOfk1.append(harmonic_value)

    for k in range(0, new_len):
        harmonic_value = 0
        for n in range(0, new_len):
            harmonic_value += (ySignal2[n] *  np.exp((-j * 2 * np.pi * k * n) / new_len))
        xOfk2.append(harmonic_value)

    # Convolution
    for i in range(new_len):
        yOfk.append(xOfk1[i] * xOfk2[i])

    # IDFT
    for n in range(0, new_len):
        harmonic_value = 0
        for k in range(0, new_len):
            harmonic_value += (1 / new_len) * (yOfk[k] * np.exp((j * 2 * np.pi * n * k) / new_len))
        convsignal.append((np.real(harmonic_value)))

    return convsignal

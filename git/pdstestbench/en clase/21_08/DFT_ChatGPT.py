#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:48:17 2024

@author: elvitu
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros
N = 64  # Número de puntos en la señal
t = np.arange(N)  # Vector de tiempo

# Señal: combinación de dos sinusoides
x = 3 * np.sin(2 * np.pi * 5 * t / N) + 2 * np.sin(2 * np.pi * 10 * t / N)

def dft(x):
    N = len(x)  # Longitud de la señal
    X = np.zeros(N, dtype=complex)  # Inicializamos la DFT con ceros (tipo complejo)

    for k in range(N):  # Para cada valor de frecuencia k
        for n in range(N):  # Para cada muestra en la señal
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    
    return X

X_manual = dft(x)

# Gráfica de la señal original
plt.figure()
plt.plot(t, x)
plt.title('Señal en el dominio del tiempo')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')

# Gráfica del espectro de frecuencias manual
freqs = np.fft.fftfreq(N)  # Vector de frecuencias
plt.figure()
plt.stem(freqs, np.abs(X_manual), use_line_collection=True)
plt.title('Espectro de frecuencias (DFT Manual)')
plt.xlabel('Frecuencia')
plt.ylabel('Magnitud')
plt.show()


xx2=(np.random.random_sample((10,)))
X_manual2 = dft(xx2)
plt.figure()
plt.plot(t, xx2)
plt.title('Señal en el dominio del tiempo')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')

# Gráfica del espectro de frecuencias manual
freqs = np.fft.fftfreq(N)  # Vector de frecuencias
plt.figure()
plt.stem(freqs, np.abs(X_manual), use_line_collection=True)
plt.title('Espectro de frecuencias (DFT Manual)')
plt.xlabel('Frecuencia')
plt.ylabel('Magnitud')
plt.show()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:54:42 2024

@author: elvitu
"""
import numpy as np
import matplotlib.pyplot as plt

#N = 8
#xx = sea una senoidal con k = 1:N/2
#myDFT( xx)
#graficar modulo y fase

N = 10
fs = 1000
k = 1
 
delta = k*(fs/N)    #respuesta espectral es fs/N
w = 2*np.pi*delta
phase = 180

t = np.arange(start=0, stop = N/fs, step=1/fs)

xx = np.sin(w*t + phase)

#Para realizar una funcion, comienzo con la palabra "def"
def mi_funcion_DFT(xx):
    N = len(xx)
    XX = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            XX[k] += xx[n]*np.exp((-2j*np.pi*(k*n))/N) 
    
    return XX


X_manual = mi_funcion_DFT(xx)

# Gráfica de la señal original
plt.figure()
plt.plot(t, xx)
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
X_manual = mi_funcion_DFT(xx2)
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

#sin usar "for"

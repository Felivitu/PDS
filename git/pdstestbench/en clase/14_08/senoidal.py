#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 21:20:18 2024

@author: elvitu
"""

import numpy as np   ##np es ponerle un nombre nada mas
import matplotlib.pyplot as plt      ##sirve para graficar, plotear

##frecuencia de N muestras que vaya de 0 a N muestras
## Para ir de 0 a 1 segundo, tiene que ir desde 0, desp 1/fs hasta N-1/fs
#PARA PLOTEAR APARTE, en la terminal usar %matplotlib qt5

N = 1000
fs = 1000
##res_esp = np.pi/2*fs/256
#k=(N/2) +2
#k = fs + (fs/N)    #vuelvo a la inicial
k = fs - (fs/N)    #igual a la inicial pero inversa, desfasada 180
#k = -(fs + (fs/N))     #con valor negativo, se puede frecuencia negativa
#k=10
#k=100
#k=(N/2)
delta = k*(fs/N)    #respuesta espectral es fs/N
w = 2*np.pi*delta
phase = 0
##phase = np.pi/2
## x = np.linspace(-np.pi, np.pi, 999)
## x = np.linspace(0, N/fs, N)
x = np.arange(start=0, stop = N/fs, step=1/fs)

## numpy.arange([start, ]stop, [step, ]dtype=None, *, device=None, like=None)
##np.sin(x)

plt.plot(x, np.sin(w*x + phase))
plt.xlabel('tiempo')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()

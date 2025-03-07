# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 10:46:58 2025

@author: Noe
"""

#GENERAR MUESTREO SENOIDAL
import numpy as np
import matplotlib.pyplot as plt

fs=1000.0 #frec muestreo
N=1000 #cantidad de muestras
Ts=1/fs
f0=100 #Hz
t=np.linspace(0,(N-1)*Ts,N)
y=np.sin(2*np.pi*f0*t)

plt.figure(1)
plt.plot(t,y)
plt.show

########

f0=1 #Hz
t=np.linspace(0,(N-1)*Ts,N)
y=np.sin(2*np.pi*f0*t)

plt.figure(2)
plt.plot(t,y)
plt.show

########

f0=400 #Hz
t=np.linspace(0,(N-1)*Ts,N)
y=np.sin(2*np.pi*f0*t)

plt.figure(3)
plt.plot(t,y)
plt.show




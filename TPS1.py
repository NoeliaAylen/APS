<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 20:57:33 2025

@author: Noe
"""

=======
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 20:57:33 2025

@author: Noe
"""
###TPS1

import numpy as np
import matplotlib.pyplot as plt

def mi_funcion_sen(vmax=1, dc=0, ff=1, ph=0, nn=1000, fs=1000.0):
    Ts = 1 / fs  # Período de muestreo
    tt = np.linspace(0, (nn - 1) * Ts, nn)  # Vector de tiempos
    xx = vmax * np.sin(2 * np.pi * ff * tt + ph) + dc  
    
    return tt, xx

# Prueba de la función con parámetros dados
tt, xx = mi_funcion_sen(vmax=1, dc=0, ff=1, ph=0, nn=1000, fs=1000)

# Graficar la señal generada
plt.plot(tt, xx)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (V)")
plt.title("Señal Senoidal")
plt.grid()
plt.show()

###EXPERIMENTOS EN CLASE


fs=1000.0 #frec muestreo
N=1000 #cantidad de muestras
Ts=1/fs
f0=500 #Hz
t=np.linspace(0,(N-1)*Ts,N)
y=np.sin(2*np.pi*f0*t)

plt.figure(1)
plt.plot(t,y)
plt.show

########

f0=999 #Hz
t=np.linspace(0,(N-1)*Ts,N)
y=np.sin(2*np.pi*f0*t)

plt.figure(2)
plt.plot(t,y)
plt.show

########

f0=1001 #Hz
t=np.linspace(0,(N-1)*Ts,N)
y=np.sin(2*np.pi*f0*t)

plt.figure(3)
plt.plot(t,y)
plt.show

######

f0=2001 #Hz
t=np.linspace(0,(N-1)*Ts,N)
y=np.sin(2*np.pi*f0*t)

plt.figure(4)
plt.plot(t,y)
plt.show

#### IMPLEMENTACIÓN DE OTRA SEÑAL
from scipy.signal import square

def mi_funcion_cuadrada(vmax=1, dc=0, ff=1, nn=1000, fs=1000.0, duty=0.5):
    tt = np.linspace(0, (nn - 1) / fs, nn)
    xx = vmax * square(2 * np.pi * ff * tt, duty) + dc
    return tt, xx

# Señal cuadrada
tt, xx = mi_funcion_cuadrada(vmax=1, ff=10, nn=1000, fs=1000, duty=0.5)
plt.figure()
plt.plot(tt, xx)
plt.title("Señal Cuadrada")
plt.grid()

>>>>>>> 95f8b17 (Subiendo notebook)

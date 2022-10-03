# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:27:05 2020

@author: Paola Morales y andres Buenaventura
"""

import sys 
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
import numpy as np
from numpy import pi
import scipy.io.wavfile as waves
import scipy.fftpack as fourier
from scipy.fftpack import fft, fftfreq
from scipy import stats # importando scipy.stats
import pandas as pd  

#%%
#primera parte carge de archivo .wav
vocal__a=[]     #crea un vector vaciddo / lista
for i in range(1,12):  # numero de archivos a cargar
    vocal_a ='a_' + str(i) + '.wav'#llama cada unos de los archivos convirtiendo i en texto
    F, S = waves.read(vocal_a) # f=frecuencia de muestreo S= muestras 
    iok1=np.nonzero(abs(S)>300) # crea una codicionque solo toma los valores mayores de 300
    S=S[iok1]#sele quita el los valores menores de 300
    #S=S/np.max(S)
    vocal__a.append(S)# se agregan auna nueva lista
#%% transformada de folier
trans=[]#lista temporal para el ciclo for 
trasF=[]#lista para guardar los valores de la tranasformada de foulier
for k in range(0,11): #for para recorrer la lista de las señales 
    trans=vocal__a[k]# llamando los valores de la listas
    se_fft=fft(trans)/2 #aplicando transformada de foulier
    se_fft=abs(se_fft)#determinando el valor absoluto de cada una de la transformada
    se_fft=se_fft/np.max(se_fft)
    trasF.append(se_fft)# guardando las nueva señales generadas


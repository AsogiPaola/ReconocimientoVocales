import sys 
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
import numpy as np
from numpy import pi
import scipy.io.wavfile as waves
import scipy.fftpack as fourier
from scipy.fftpack import fft, fftfreq
#%%
#primera parte carge de archivo .wav
vocal__a=[]     #crea un vector vaciddo / lista
for i in range(1,65):  # numero de archivos a cargar
    vocal_a ='a_' + str(i) + '.wav'#llama cada unos de los archivos convirtiendo i en texto
    F, S = waves.read(vocal_a) # f=frecuencia de muestreo S= muestras 
    iok1=np.nonzero(abs(S)>300) # crea una codicionque solo toma los valores mayores de 300
    S=S[iok1]#sele quita el los valores menores de 300
    vocal__a.append(S)# se agregan auna nueva lista
#%%  transformada de fourier
trans=[]#lista temporal para el ciclo for 
trasF=[]#lista para guardar los valores de la tranasformada de foulier
for k in range(0,64): #for para recorrer la lista de las señales 
    trans=vocal__a[k]# llamando los valores de la listas
    se_fft=fft(trans)#aplicando transformada de foulier
    se_fft=abs(se_fft)#determinando el valor absoluto de cada una de la transformada
    trasF.append(se_fft)# guardando las nueva señales generadas
#%%  creacion de la frecuencia 
freQ=[]  #lista para guardar la frecuencia de cada señal 
NFFT = 1020 
for h in range(0,64):#for para recorrer la lista 
    N=len(vocal__a[h])       # se calcula el tamaño de cada señal
    f = np.arange(0,(F/2)+0.1-(F/N),F/N) # se calcula frecuencia de con el tamaño determinado de cada una de la señal
    frq=fourier.fftfreq(N,F) # se determina la frecuencia 
    frq=fourier.fftshift(frq)
    freQ.append(frq)# se guada en una nueva lista 
#%%
for j in range(0,5): 
    plt.figure(str(j))
    plt.xlabel('TIEMPO');plt.ylabel('FRECUENCIA'); plt.title('ESPECTOGRAMA_A')
    Pxx, freqs, t_e, im = specgram(vocal__a[j], NFFT=NFFT, Fs=8000, noverlap=1000); #el tiempo, 
    #pxx es 
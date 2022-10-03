
import sys 
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
import scipy.io.wavfile as waves
import scipy.fftpack as fourier
from scipy.fftpack import fft, fftfreq
from sklearn.preprocessing import normalize


vocal_a ='u9.wav'
F, S = waves.read(vocal_a)
plt.figure(5)
#plt.plot(S)

#L=len(Ns)
T=1/F
#plt.plot(S)
plt.title('SEÑAL_VOCAL_U')
plt.xlabel('TIEMPO(Seg)')
plt.ylabel('AMPLITUD')
#G=fft(S) 
#G=abs(G)
se_fft=fft(S)/2 #aplicando transformada de fouier
se_fft=abs(se_fft) # valor absoluto
#h = ls.T
#frq = fftfreq(fs)
plt.plot(se_fft)

 
 # =============================================================================

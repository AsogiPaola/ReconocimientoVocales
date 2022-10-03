import sys 
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
#%%  CARACTERISTICAS
#  MEDIA
media__a=[]; desFT__a = [] ; max__a=[];
media__e=[]; desFT__e = [] ; max__e=[];
media__i=[]; desFT__i = [] ; max__i=[];
media__o=[]; desFT__o = [] ; max__o=[];
media__u=[]; desFT__u = [] ; max__u=[];
 
for l in range (0,64):
    media_a = trasF__a[l]
    media_a = np.mean(media_a)
    desv_a=np.std(trasF__a[l])
    max_a = np.max(trasF__a[l])
    max__a.append(max_a)
    desFT__a.append(desv_a)
    media__a.append(media_a)

    media_e = trasF__e[l]
    media_e = np.mean(media_e)
    desv_e=np.std(trasF__e[l])
    max_e = np.max(trasF__e[l])
    max__e.append(max_e)
    desFT__e.append(desv_e)
    media__e.append(media_e)

    media_i = trasF__i[l]
    media_i = np.mean(media_i)
    desv_i=np.std(trasF__i[l])
    max_i = np.max(trasF__i[l])
    max__i.append(max_i)
    desFT__i.append(desv_i)
    media__i.append(media_i)    

    media_o = trasF__o[l]
    media_o = np.mean(media_o)
    desv_o=np.std(trasF__o[l])
    max_o = np.max(trasF__o[l])
    max__o.append(max_o)
    desFT__o.append(desv_o)
    media__o.append(media_o)

    media_u = trasF__u[l]
    media_u = np.mean(media_u)
    desv_u=np.std(trasF__u[l])
    max_u = np.max(trasF__u[l])
    max__u.append(max_u)
    desFT__u.append(desv_u)    
    media__u.append(media_u)
    
#%%
plt.plot(max__a,desFT__a,'.r')

#plt.plot(max__u,desFT__u,'.m')

#%%
plt.plot(media__a,'.r')
plt.plot(desv,'.k')
 #el tamaño






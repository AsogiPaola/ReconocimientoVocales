# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:29:31 2020

@author: Paola Morales
"""
import graphedit as gph
import numpy as np
import scipy.stats as sta
import scipy.spatial as spa

#gaussiana una dimension 
mu1=4.
std1=.5
gaussiana= sta.norm(mu1, std1)  #crear gaussiona
datos_gaussianos=gaussiana.rvs(1000)  #1000 datos distribuidos de manera gaussiana

Gg1=gph.BGraph(1, 2, vec=1, shy=False, shx=False)  # 1(fila) y 2columnas
# axs para el tamaño, o regla de la grafica matricial (0)vectorial(1)
#shy y shx para compartir los x y y
Gg1.axs[0].plot(datos_gaussianos) #el objeto Gg1 tiene una propiedad que son los axs, 
#y que la haga en el primer axs, y el primer elemento es el 0 

histo_gauss=np.histogram(datos_gaussianos, 20)
Gg1.axs[1].plot(histo_gauss[1][1:], histo_gauss[0])

#Gg1.axs[1].bar(histo_gauss[1][1:], histo_gauss[0], width=0.1)

x_1=np.array([0.2,1.3])
x_2=np.array([2.2,-1.3])

mu=np.array([0.,1.])
S=np.array([[1.,0.],[0.,1.]])

norm=sta.multivariate_normal(mu,S)

nx_1=norm.pdf(x_1)
print(nx_1)


nx_2=norm.pdf(x_2)
print(nx_2)



# - Crear x
# - funcion g(x)
# - funcion de costo J(w)
# - funcion perceptron
# import sys
import numpy as np
import scipy.stats as sta
# import scipy.spatial as spa
# import matplotlib.pyplot as plt
import graphedit as gph


## Definicion funcion g(x)
def g(w, x_i):
    return np.dot(w, x_i)


# Funcion de costo
# Si un punto esta mal calsificado g(x)*clase<0
def J(w, x, clase):
    Jx = 0.
    for n in np.arange(x.shape[1]):
        # print x[n]
        # print clase[n]
        if g(w, x[:, n])*clase[n] < 0.:
            Jx = Jx - g(w, x[:, n])*clase[n]
    return Jx



# Encuentre w(t+1)
# La función delta es igual a multiplicar por el inverso del signo
# de la clase
def wplus1(w, x, rho, clase):
    DJx = 0.
    for n in np.arange(x.shape[1]):
        if g(w, x[:, n])*clase[n] < 0.:
            DJx = DJx + x[:, n]*clase[n]
    return w + rho*DJx


## Generacion de los datos para entrenar
# Define las gaussinas
mu_1 = np.array([0., 20.])
mu_2 = np.array([5., 20.])
S_1 = S_2 = np.array([[1., 0.7], [0.7, 1.]])
norm_2 = sta.multivariate_normal(mu_1, S_1)
norm_1 = sta.multivariate_normal(mu_2, S_2)

# Generar los datos
data_1 = norm_1.rvs(100)
data_2 = norm_2.rvs(100)

GPc = gph.BGraph(1, 1, shx=False, shy=False, vec=1,
                               Dx=0.1, Dxr=.01, Dxl=0.075, Dyb=0.12)

GPc.axs[0].plot(data_1[:, 0], data_1[:, 1], 'sb')
GPc.axs[0].plot(data_2[:, 0], data_2[:, 1], '.r')
GPc.set_figure(l_width=3, ax_size=20, tx_size=20,
              lg_size=25, m_size=15)

## adecuar los datos
x1 = data_1[:, 0]
y1 = data_1[:, 1]
clase1 = np.ones(x1.size)
x2 = data_2[:, 0]
y2 = data_2[:, 1]
clase2 = -1*np.ones(x2.size)

unos = np.ones(x1.size+x2.size)
x1 = np.hstack((x1, x2))
y1 = np.hstack((y1, y2))
x = np.vstack((x1, y1, unos))
clase = np.hstack((clase1, clase2))

## usar el perceptron
# punto de prueba
rho = 0.01
w = np.array([1.2, 1.2, -23.])
w = np.array([-.6172132,
              3.7068999,
              -1.00000000e+00])
Je = np.array([])
N = 40
for i in np.arange(N):
    wp1 = wplus1(w, x, rho, clase)
    # print(wp1)
    w = wp1
    Je = np.hstack((Je, J(w, x, clase)))

GEp = gph.BGraph(1, 1, shx=False, shy=False, vec=1,
                               Dx=0.1, Dxr=.01, Dxl=0.075, Dyb=0.12)
GEp.axs[0].plot(Je)
GEp.set_figure(l_width=3, ax_size=20, tx_size=20,
              lg_size=25, m_size=15)

## pruebas
x_1 = np.array([6., 20., 1])
x_1 = np.array([1.92, 20., 1])
print(g(w, x_1))
GPc.axs[0].plot(x_1[0], x_1[1], 'sg')
x_plot = np.linspace(-3, 7, 10)
y_plot = -(x_plot*w[0]-w[-1])/w[1]
GPc.axs[0].plot(x_plot, y_plot, '--k')
GPc.set_figure(l_width=3, ax_size=20, tx_size=20,
              lg_size=25, m_size=15)
# w = np.array([1.2, 1.2, -23.])
# i = 85
# x_i = x[:, i]
# print(x_i)
# # indice= np.arange(clase.size)
# for i in np.arange(clase.size):
#     print(g(w, x[:, i]))

#     # print(g(w, x[:, i]))
# # for x_i, clase_i in zip(x, clase):
# #     print(x_i)
# #     print(clase_i)
# #     # print(g(w, x_i))

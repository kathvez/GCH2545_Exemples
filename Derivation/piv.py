# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:53:20 2023

@author: Kath
"""

import numpy as np
from matplotlib import pyplot as  plt


#Variables qui contient le nom des fichiers contenant les position des particules
f_0 = 'temps_0.dat'
f_1 = 'temps_1.dat'

#Stockage des positions des particules
x_0 = np.loadtxt(f_0)
x_1 = np.loadtxt(f_1)

#Temps, generalement devrait etre lu d'un fichier
t_0=10
t_1=10.001

# Calcul des vecteurs vitesse par dérivation avant
v_avant = (x_1 - x_0) / (t_1 - t_0)

# Tracer le graphique des vecteurs de vitesse
fig, fig = plt.subplots()
plt.xlim(0, 1)
scale = 25
plt.quiver(x_0[:, 0], x_0[:, 1], v_avant[:, 0], v_avant[:, 1], scale=scale, linewidth=3)
plt.show()
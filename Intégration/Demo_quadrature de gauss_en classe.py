# -*- coding: utf-8 -*-
"""
Démonstration en classe de la quadrature de Gauss-Legendre
Quadrature en deux points VS méthode pour trapèze

@author: Kath
"""

import numpy as np

#Paramètres pour la quadrature de Gauss-Legendre à deux points

w=np.zeros(2)
t=np.zeros(2)
w[0] = 1.0
w[1] = 1.0
t[0] = -np.sqrt(1/3)
t[1] = -t[0]

# Bornes d'intégration
a = 0
b = 1

# Pas d'intégration (pour la méthode par trapèzes)
n = int(1e6)   # nombre de points de données 
N = n - 1  # nombre d'intervalles

# Polynome à intégrer 
f = lambda x: 3 * x**3 + x**2 - x + 9

# Changement de bornes
g = lambda t: f(((b-a) * t + b + a)/2) * (b - a) / 2

# Intégration par trapèzes de la fonction f(x) entre a et b
x = np.linspace(a, b, n)
I_trap = np.trapz(f(x), x)
print(f"Intégration par trapèzes: {I_trap}")

# Intégration (de la fonction g(t) entre les bornes -1 et 1) par la quadrature
# de Gauss-Legendre
I_gauss = w[0] * g(t[0]) + w[1] * g(t[1])
print(f"Intégration par Gauss-Legendre: {I_gauss}")

#Calculer la différence entre les deux valeurs 
diff=I_trap-I_gauss
print(f"Différence entre les deux méthodes:{diff}")
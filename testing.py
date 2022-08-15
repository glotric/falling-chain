import numpy as np
import math
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

P0 = np.array((0.0, 0.0))   # levo sidrisce
P1 = np.array((5.0, 1.0))   # desno sidrisce
L = 6    # dolzina vrvi
m = 3    # dolzinska gostota mase
g = 1   #teznostni pospesek
t = 10


d = abs(P0[0] - P1[0])
h = abs(P0[1] - P1[1])

if L <= np.sqrt(d**2 + h**2):
    print('Prekratka vrv')
else:
    pass


def catenary(a):
    return a * np.sinh(d/(2*a)) + np.arctanh(h/L) + a * np.sinh(d/(2*a)) - np.arctanh(h/L) - L

a = fsolve(catenary, 1) # najdemo tapravo krivuljo
print(f'a =', a)

d1 = a * (d/(2*a) + np.arctanh(h/L))
d0 = d - d1

if P1[1] >= P0[1]:
    xi = d0
    xf = d1

elif P1[1] < P0[1]:
    xi = d1
    xf = d0


x = np.linspace(-xi, xf, 500)
y = np.zeros_like(x)

y = a * np.cosh((x)/a)

h_max = a * (math.cosh(d1 / a) - 1)
print(h_max)

y = y - y[0]
x = x + xi





def xy_to_phi(x, y, n, L): # x y are same size arrays, n is number of segments wanted, L is the total lenght of chain
    l = L / n
    phi = np.zeros(n)
    nov_x = np.zeros(n)
    nov_y = np.zeros(n)

    i = 0
    j = 0
    k = 0

    while i < len(x) and j < len(x):
        while np.sqrt((x[j] - x[i])**2 + (y[j] - y[i])**2) < l:
            j += 1
            
        
        nov_x[k] = x[i]
        nov_y[k] = y[i]
        k += 1
        i = j

    return nov_x, nov_y


x_nov, y_nov = xy_to_phi(x, y, 100, L)
plt.plot(x_nov, y_nov)
plt.show()


import numpy as np
import matplotlib.cm as cm

def suma(a,b):
    return a+b

def roznica(a,b):
    return a-b

def iloczyn(a,b):
    return a*b

mapaFunkcji = {"suma":suma, "roznica":roznica, "iloczyn":iloczyn}

a=4
b=5
operacja = "suma"
#print mapaFunkcji[operacja]


x = np.linspace(0,1,10)
y = np.linspace(0,1,10)

X,Y = np.meshgrid(x,y)

Z = np.sin(X*Y)


import matplotlib.pyplot as plt
plt.figure()
cs = plt.contourf(X,Y,Z,30, cmap=cm.winter)
#plt.plot(x,y, color="red")


plt.show()

#Lab 2

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


m = 1
k=10
x10 = [0,0]
x20 = [10,0]
l0 = 10
u10 = [0,5]
u20 = [-3,3]



def rhs(Y0, t):
    x1 = Y0[2:3]
    u1 = Y0[:2]
    x2 = Y0[6:]
    u2 = Y0[4:6]
    r = x2 - x1
    dlr = np.linalg.norm(r)
    dYdt = np.zeros(8)
    dYdt[:2] = r*k/m*(1.-l0/dlr)
    dYdt[2:4] = u1
    dYdt[4:6] = r*k/m*(1. -l0/dlr)
    dYdt[6::] = u2
    dYdt[3] += -9.81
    dYdt[7] += -9.81
    return dYdt

time = np.linspace(0,5,100)
y0 = np.zeros(8)
y0[:2] = u10
y0[2:4] = x10
y0[4:6] = u20
y0[6:] = x20
y = odeint(rhs, y0, time )

fig = plt.figure()

plt.plot(y[:,2], y[:,3],"b-")
plt.plot(y[:,6], y[:,7],"g-")

plt.show()

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import odeint

K = 0.003730392 #N/rad
m = 0.004257 #kg
g = 1.62 #m/s^2
L = 0.17 #m

R_inner = 0.0014 #m
R_outer = 0.002 #m
J = (m/12)*(3*(R_inner**2 + R_outer**2) + L**2)
print(J)
#https://amesweb.info/inertia/hollow-cylinder-moment-of-inertia.aspx

def f(u,x):
    return(u[1], (K*u[1] - 0.5*m*L*g)/J)


y0 = [math.pi/2, 0] #Initial conditions of theta and dtheta/dt
xs = np.arange(0,0.025,0.000001) #Time span
print(xs[-1])
us = odeint(f, y0, xs)
ys = us[:,0]
plt.plot(xs, ys,'-')
plt.ylim([0, math.pi/2])
plt.xlabel("Time [s]")
plt.ylabel("Angle [rad]")
plt.show()

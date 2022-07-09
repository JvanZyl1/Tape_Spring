import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri


#length = int(input("Length: 17cm, 34cm, 51cm or 68cm"))
E = 69*(10**9)
L = 0.17 #m
t = np.arange(0.5, 1, 0.1)*(10**(-3))
radiusmax = 4.0 #Machining constraint R/d = b/a >= 1.25
b = np.arange(1.0, radiusmax, 0.5)*(10**(-3))
a = np.arange(0.1, radiusmax/1.25, 0.5)*(10**(-3))
tres, ares, bres, Pxres, Pyres, areas, sigmaxr, sigmayr = [], [], [], [], [], [], [], []
bucklingload = 20*9.81
for i in range(len(t)):
    for j in range(len(a)):
        for k in range(len(b)):
            Ix = math.pi/4 * a[j]**3 * t[i] * (1 + (3*b[k])/a[j]) * 1/2
            Iy = math.pi/4 * a[j]**3 * t[i] * (1 + (3*a[j])/b[k]) * 1/2
            Px = (math.pi**2 * E * Ix)/(L**2)
            Py = (math.pi**2 * E * Iy)/(L**2)
            Area = math.pi*(b[k]*a[j] - (b[k]-t[i])*(a[j]-t)[i]) # https://rechneronline.de/pi/elliptical-ring.php
            sigmax = Px/Area
            sigmay = Py/Area
            resultx = [t[i], a[j], b[k], Px]
            resulty = [t[i], a[j], b[k], Py]
            tres.append(t[i]), ares.append(a[j]), bres.append(b[k]), Pxres.append(Px), Pyres.append(Py), areas.append(Area), sigmaxr.append(sigmax), sigmayr.append(sigmay)
            
            
print(max(Pxres), max(Pyres), max(sigmaxr), max(sigmayr))
npts = 20000
ngridx = 1000
ngridy = 1000
x = ares#a
y = bres #b
z = Pxres #Px

fig, (ax2) = plt.subplots(nrows=1)
xi = np.linspace(0, (radiusmax/1.25)*(10**(-3)), ngridx)
yi = np.linspace(0, radiusmax*(10**(-3)), ngridy)
triang = tri.Triangulation(x, y)
interpolator = tri.LinearTriInterpolator(triang, z)
Xi, Yi = np.meshgrid(xi, yi)
zi = interpolator(Xi, Yi)

ax2.tricontour(x, y, z, levels=20, linewidths=0.5, colors='k')
cntr2 = ax2.tricontourf(x, y, z, levels=20, cmap="RdBu_r")

fig.colorbar(cntr2, ax=ax2)
ax2.plot(x, y, 'ko', ms=3)
ax2.set(xlim=(0, (radiusmax/1.25)*(10**(-3))), ylim=(0, radiusmax*(10**(-3))))
ax2.set_title("A contour plot for PA3")

plt.subplots_adjust(hspace=0.5)
plt.xlabel("a: Max Depth")
plt.ylabel("b: Radius")
plt.show()






#https://www.sciencedirect.com/topics/engineering/critical-buckling-load
#https://www.researchgate.net/figure/a-A-hollow-cylinder-with-radius-R-and-wall-thickness-t-with-the-second-moment-of-area_fig2_318444188
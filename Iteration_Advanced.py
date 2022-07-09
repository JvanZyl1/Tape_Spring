#### TAPE-SPRING SIZING PROGRAM by Jonathan Robert van Zyl ####

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri

QSL = 20 * 9.81
tf = np.arange(0.6, 4.1, 0.1)
ans, tres, ares, bres, Pxres, Pyres, areas, sigmaxr, sigmayr, tfres, abres, defa, buck , omegax, omegay, omega1x = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
E = 69*(10**9)
L = float(input("What is the length of the rod m? N.B. Ideally multiples of 0.17m: 0.17, 0.34, 0.51, 0.68."))
Buckling = False
rho = 2710 #For aluminium


####################Calculating: area, moment of inertia, deflection of cantilever beam, critical bukcling load and stress, buckling occurance, natural frequencies ####################
for y in range(len(tf)):
    t = np.arange(0.5, tf[y], 0.1)*(10**(-3))
    radiusmax = 20.0 # mm
    delta = radiusmax/10 #Step count
    b = np.arange(1.0, radiusmax, delta)*(10**(-3))
    a = np.arange(0.1, radiusmax/1.25, delta)*(10**(-3)) #Machining constraint R/d = b/a >= 1.25
    bucklingload = 20*9.81
    for i in range(len(t)):
        for j in range(len(a)):
            for k in range(len(b)):
                Ix = math.pi/4 * a[j]**3 * t[i] * (1 + (3*b[k])/a[j]) * 1/2
                Iy = math.pi/4 * a[j]**3 * t[i] * (1 + (3*a[j])/b[k]) * 1/2#https://www.researchgate.net/figure/a-A-hollow-cylinder-with-radius-R-and-wall-thickness-t-with-the-second-moment-of-area_fig2_318444188
                Px = (math.pi**2 * E * Ix)/(L**2)#https://www.sciencedirect.com/topics/engineering/critical-buckling-load
                Py = (math.pi**2 * E * Iy)/(L**2)
                Area = math.pi*(b[k]*a[j] - (b[k]-t[i])*(a[j]-t)[i]) # https://rechneronline.de/pi/elliptical-ring.php
                sigmax, sigmay = Px/Area, Py/Area
                fa = QSL*Area #To get force from deflection, take maximum QSL (20 g's for ADS), and then F = stress*A
                defax = fa*L**3 / (3*E*Ix)
                ratio = b[k]/a[j]
                if fa>=Px or fa>=Py:
                    Buckling == True
                m = abs(rho*Area*L)
                wxconstant, wyconstant = math.sqrt((E*Ix)/(m*L**4)), math.sqrt((E*Iy)/(m*L**4)) #https://vlab.amrita.edu/?sub=3&brch=175&sim=1080&cnt=1
                wx = [1.875**2 * wxconstant, 4.694**2 * wxconstant, 7.855**2 * wxconstant]
                wy = [1.875**2 * wyconstant, 4.694**2 * wyconstant, 7.855**2 * wyconstant]
                omega1x.append(wx[0]), omegax.append(wx), omegay.append(wy), buck.append(Buckling), defa.append(defax), tres.append(t[i]), ares.append(a[j]), bres.append(b[k]), Pxres.append(Px), Pyres.append(Py), areas.append(Area), sigmaxr.append(sigmax), sigmayr.append(sigmay), tfres.append(tf[y]), abres.append(ratio)
                GG = [t[i], a[j], b[k], Px, Py, Area, sigmax, sigmay, tf[y], ratio, defa, Buckling]
                ans.append(GG)
                
#####Buckling Check##### - This now makes counter plot one obsolute
Buckling_Instances_number = np.count_nonzero(buck)
if Buckling_Instances_number == 0:
    print("No buckling occurs")
else:
    print("Buckling occurs, in ", Buckling_Instances_number, "Number of cases")
########################


######### Maximum Deflection setting
angle_pre_buckling = 5 * 2 * math.pi / 180 #5 degrees maximum angle of displacement for tape measure, this gives an approximation
maximum_deflection = L * math.sin(angle_pre_buckling)
t2, ratio2, defa2 = [], [], []
for q in range(len(defa)):
   if defa[q]<= maximum_deflection:
       t2.append(tres[q]), ratio2.append(abres[q]), defa2.append(defa[q])
####################

######## Vibration frequency ignorance, i.e. to only get danger shape
freq_highpass = 2000#From which all frequencies above are ignored
t3, ratio3, freq3 = [], [], []
for w in range(len(omega1x)):
    if omega1x[w] <= freq_highpass:
        t3.append(tres[w]), ratio3.append(abres[w]), freq3.append(omega1x[w])
#####################

#######Contour Plotting
npts = 50000
ngridx = 10000
ngridy = 10000
bamax, bamin = 2, 1.25 #Manufacturing conditions
print("1: Program to find the critical buckling loads, in x")
print("2: To find the deflection of the tape spring, in x")
print("3: To find the vibration spectrum of the tape spring, in x")
question = float(input("Which number?"))
xlab = "'t': Thickness m"
ylab = "'b/a = R/d' ratio"
if question == 1:
    x = tres#t
    y = abres #b/a = R/d
    z = Pxres #Pxres
    tit = "The Critical buckling for a", L ,"m long tape spring"
    xmaxy, ymaxy, yminy = 4.0*10**(-3), bamax, bamin #The macnufacturing condition, will 2 b/a as effects neglate after
if question == 2:
    x = t2
    y = ratio2
    z = defa2
    tit = "The Deflection of a", L, "m long tape spring at 100kN, for a maximum deflection angle of 5 degrees"
    xmaxy, ymaxy, yminy = (1.25*max(t2)), bamax, bamin
if question == 3:
    x = t3#t
    y = ratio3 #b/a = R/d
    z = freq3
    tit = "The Natural Frequency for a", L, "m long tape spring"
    xmaxy, ymaxy, yminy = (1.25*max(t3)), bamax, bamin #The macnufacturing condition, will 2 b/a as effects neglate after

fig, (ax2) = plt.subplots(nrows=1)
xi = np.linspace(0, xmaxy, ngridx)
yi = np.linspace(yminy, ymaxy, ngridy)
triang = tri.Triangulation(x, y)
interpolator = tri.LinearTriInterpolator(triang, z)
Xi, Yi = np.meshgrid(xi, yi)
zi = interpolator(Xi, Yi)

ax2.tricontour(x, y, z, levels=50, linewidths=0.5, colors='k') #Notes tweake the levels for accuracy and zoom, aim to minimise
cntr2 = ax2.tricontourf(x, y, z, levels=50, cmap="RdBu_r")

fig.colorbar(cntr2, ax=ax2)
ax2.plot(x, y, 'ko', ms=3)
ax2.set(xlim=(0, xmaxy), ylim=(yminy, ymaxy))
ax2.set_title(tit)

plt.subplots_adjust(hspace=0.5)
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.show()
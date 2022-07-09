import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri


####Step 2 - Final value picker ####
bbya = float(input("What is the chosen value of the ratio R/d, b/a?"))
thickness = float(input("What is the choosen thickness?"))
radiusmax = 20.0 # mm
delta = radiusmax/1000 #Step count
b = np.arange(1.0, radiusmax, delta)*(10**(-3))
a = b/bbya
QSL = 20 * 9.81
E = 69*(10**9)
rho = 2710
L = float(input("What is the length of the rod m? N.B. Ideally multiples of 0.17m: 0.17, 0.34, 0.51, 0.68."))
Buckling = False


##### Re-calculate values for choosen radius and diameter
answers = []
for i in range(len(b)):
    Ix = math.pi/4 * a[i]**3 * thickness * (1 + (3*b[i])/a[i]) * 1/2
    A = 2*b[i]*thickness*(1-1/(math.pi))
    ybar = 1/(2*A) * ((thickness**2 + 2*a[i]*thickness)*b[i] + 2*b[i]*thickness**2)
    h = a[i]/2 - ybar
    Area = 2* (math.pi*(b[i]*a[i] - (b[i]-thickness)*(a[i]-thickness))) # https://rechneronline.de/pi/elliptical-ring.php
    m = abs(rho*Area*L)
    Inertiax = 2*(Ix + m* h**2)
    Px = (math.pi**2 * E * Inertiax)/(L**2)#https://www.sciencedirect.com/topics/engineering/critical-buckling-load
    sigmax = Px/Area
    fa = QSL*Area #To get force from deflection, take maximum QSL (20 g's for ADS), and then F = stress*A
    defax = fa*L**3 / (3*E*Ix)
    if fa>=Px:
        Buckling == True
    wxconstant = math.sqrt((E*Ix)/(m*L**4)) #https://vlab.amrita.edu/?sub=3&brch=175&sim=1080&cnt=1
    wx = [1.875**2 * wxconstant, 4.694**2 * wxconstant, 7.855**2 * wxconstant]
    Results = [a[i], b[i], Px, Area, sigmax, defax, Buckling, m, wx[0]]
    answers.append(Results)

A = []
angle_pre_buckling = 5 * 2 * math.pi / 180 #5 degrees maximum angle of displacement for tape measure, this gives an approximation
maximum_deflection = L * math.sin(angle_pre_buckling)
xax, yax = [], []
for j in range(len(answers)):
    working = True
    (answers[i]).append(working)
    if answers[i][6] == True: #Buckling check
        working = False
    elif answers[i][5]>= maximum_deflection: #Deflection check
        working = False
    #elif answers[i][7] <= mass: #Ignore mass change as all similar mass's anyways
     #   A.append(answers[i][:])
    else:
        working = True
    
   # if working == True: #Ignore freq change as all similar f0 anyways
    #    x_axis = answers[i][1]
     #   y_axis = answers[i][-1]
      #  xax.append(x_axis), yax.append(y_axis)


#plt.plot(xax, yax)
#plt.show()


        
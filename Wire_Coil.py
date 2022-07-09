import math
import numpy as np
import matplotlib.pyplot as plt

##All units are in millimetres##
t =  1.0#Thickness of Tape Spring
wt = 0.25 #Maximum Thickness of Connecting Wires
N = np.arange(1, 8, 1) #Number of turns
W = 2*t + wt #Wire diameter
S = 0 #Turn spacing
Di = np.arange(7.5, 25 + 0.1, 0.1) #inner diameter of wire coil
Outcomes = []
for i in range(len(N)):
    for j in range(len(Di)):
        Do = Di[j] + 2*N[i]*(W+S) - 2*S #Outer Diameter
        A = (Di[j] + N[i]*(W+S))/2 #Random Constant
        L = (N[i]**2 + A**2)/(30*A - 11*Di[j]) #Length of wire [m]
        List = [Di[j], N[i], Do, A, L]
        Outcomes.append(List)
        
###https://www.deepfriedneon.com/tesla_f_calcspiral.html
L1, L2, L3, L4, L5, L6, L7 = [],[],[],[],[],[], []
for k in range(len(Outcomes)):
    if Outcomes[k][1] == 1:
        L1.append(Outcomes[k][4])
    elif Outcomes[k][1] == 2:
        L2.append(Outcomes[k][4])
    elif Outcomes[k][1] == 3:
        L3.append(Outcomes[k][4])
    elif Outcomes[k][1] == 4:
        L4.append(Outcomes[k][4])
    elif Outcomes[k][1] == 5:
        L5.append(Outcomes[k][4])
    elif Outcomes[k][1] == 6:
        L6.append(Outcomes[k][4])
    else:
        L7.append(Outcomes[k][4])

plt.plot(Di, L1, Di, L2, Di, L3, Di, L4, Di, L5, Di, L6, Di, L7)
plt.legend(["1 turn", "2 turns", "3 turns", "4 turns", "5 turns", "6 turns", "7 turns"])
plt.plot([7.5, 25], [0.51, 0.51], 'k-', lw=2)
plt.xlabel("Inner Diameter")
plt.ylabel("Length of Coil")
plt.title("Sizing the Tape-Spring Coil")
plt.show()

Dis, Ns, Ws = 10.00, 4, 1.25
Dos = Dis + 2*Ns*(Ws)#Outer Diameter
print(Dos)


import math

boxdim = 26 #mm
rho_al = 0.00271#g/mm^-3
rho_3D = 0.00115 #1.15*((10**(-3))**3)- kg/mm^-3 - Nylon filament
R_flat = 1.75 #mm
t_tape = 0.5 #mm
W = 1.25 #mm
Di = 10 #mm
boxwidth = 41 #mm

tape_mass = (rho_al*(2*R_flat)*t_tape*(51+0.5*boxdim+2))*2
tape_x = 2 + 0.5*boxdim + 0.5*W
tape_y = 0.5*(51 + 0.5*boxdim + 2) + 0.5*boxdim
#box_mass = rho_3D*(2*(boxdim+2)**2 + (boxwidth+2)*(2+boxdim) + (boxwidth+4)*(boxdim+2)+ math.pi*(5**2-4**2)*boxwidth
box_mass = rho_3D*(2*((boxwidth +4)*(boxdim+2) + (boxwidth +4)*(boxdim)*2 + 2*((boxdim + Di)/2)**2 *2) + math.pi*(5**2 - 4**2)*boxwidth)
#box_mass = rho_3D*(4*(boxdim**2) + 8*boxdim*boxwidth + math.pi*(5**2 - 4**2)*0.5*boxwidth)
#box_x =0.5*boxdim + 2
box_x = rho_3D*(2*((boxwidth +4)*(boxdim+2))*1 + 2*rho_3D*(2+ 0.5*(boxdim+Di))*((boxdim + Di)/2)**2 *2) + rho_3D*(boxwidth +4)*(boxdim)*2*(2 + 0.5*(boxdim)
#box_x = ( (boxdim*boxwidth*2*rho_al) + (2*2*(0.5*(boxdim + Di))*rho_al*(2 + 0.25*(boxdim + Di))) + (rho_al*(0.5*boxdim +2)*(boxdim*boxwidth*2)))/box_mass
box_y = 2
total_mass = box_mass + tape_mass
print("box mass [g]", box_mass,"tape mass [g]",tape_mass,"total mass [g]", total_mass)
xbar = ((tape_mass*tape_x)+(box_mass*box_x))/(total_mass)
ybar = ((tape_mass*tape_y)+(box_mass*box_y))/(total_mass)
print(xbar, "mm")
print(ybar, "mm")

                                                                                                                                                                                                                                            

import bio

#  problem from Bioelectricity course Lecture 1 section 11
#  2 mA source and sink 1 mm apart in x direction
#  resistivity is 100.5 ohm-cm 
#  what is potential at distance 10 mm from one source in the z direction (y= 0)
Io = 2E-3
r = 10E-3
d = 1E-3
rx = bio.length((d,0,r))

rho =  100.5 * 1.0E-2 # ohms-m
sigma = 1.0 / rho

phi1 = bio.monopole_potential(Io,sigma,r)
phi2 = bio.monopole_potential(-Io,sigma,rx)
potential = phi1 + phi2 
print r,rx,sigma,phi1,phi2,potential,"Volts"


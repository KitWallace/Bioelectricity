import math
import bio

#  problem from Bioelectricity course Lecture 1 section 11
#  2 mA source and sink 1 mm apart in x direction
#  resistivity is 100.5 ohm-cm 
#  what is potential at distance 10 mm from one source in the z direction (y= 0)
#
#  compare the model based on two monopoles with the dipole approximation
#  varying the separation d

Io = 2E-3
r = 10E-3
d = 1E-3
rho =  100.5 * 1.0E-2 # ohms-m
sigma = 1.0 / rho

for i in range(1,7) :
  rx = bio.length((d,0,r))
  theta = math.asin(d / 2 / r)
  m1_potential = bio.monopole_potential(Io,sigma,r) + bio.monopole_potential(-Io,sigma,rx) 
  m2_potential = bio.dipole_potential(Io,sigma,r, d, math.radians(theta))
  print r,rx, theta, m1_potential,m2_potential
  d = d / 10




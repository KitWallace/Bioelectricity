import math

# fibre
diameter  = 10E-6 # 10 microns
length = 100E-6  # 100 micros
area = math.pi * diameter * length
print "area=",area

Cm = 1E-6/ 1E-4   # 1 micro farad / cm2  in F/m2
Rm = 1500 * 1E-4  # ohm - cm2  in ohm - m2
print "Rm=",Rm, "Cm=",Cm

R = Rm / area 
C = Cm * area
print "R=",R, "C=",C

RC = R * C   # timeconstant 
print "RC=", RC * 1E6 ,"ms"


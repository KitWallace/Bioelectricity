import math

# fibre
diameter  = 10E-6 # 10 microns
length = 100E-6  # 100 micros
area = math.pi * diameter * length
print "area=",area

Cm = 1E-6  # 1 micro farad / cm2
Rm = 1500  # 1500 ohm - cm2  
print "Rm=",Rm, "Cm=",Cm, " in cgs units"

# convert to MKS
Cm_mks = 1E-6/ 1E-4   #  in F/m2
Rm_mks = 1500 * 1E-4  # in ohm - m2
print "Rm=",Rm_mks, "Cm=",Cm_mks," in MKS units"

R = Rm_mks / area 
C = Cm_mks * area
print "R=", round(R * 1E-6,2),"M ohms " "C=",round(C * 1E12,2), "picoFarads"

RC = R * C   # timeconstant 
print "RC=", RC * 1E6 ,"ms"


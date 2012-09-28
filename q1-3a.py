import bio

# A dipole current source consists of 2 point sources +Io and -Io. 
# These sources are placed at positions (0,0,5) and (0,0,-5) meters, 
# respectively. Io= 3 A, and the conductivity is 4 S/m.
# What is the resulting potential at point (2,4,0) meters? 

Io = 3      # Amp
sigma = 4  # S / m
r1 = bio.length(bio.subtract((0,0,5),(2,4,0)))  # m
r2 = bio.length(bio.subtract((0,0,-5),(2,4,0)))  # m

phi1 = bio.monopole_potential(Io,sigma,r1)
phi2 = bio.monopole_potential(-Io,sigma,r2)
potential = phi1 + phi2 
print r1,r2,sigma,phi1,phi2,potential,"Volts"


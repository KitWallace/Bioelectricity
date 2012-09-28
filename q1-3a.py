import bio

Io= 3      # Amp
sigma = 4  #S / m
r1 = bio.distanceBetween((0,0,5),(2,4,0)) # m
r2 = bio.distanceBetween((0,0,-5),(2,4,0))  # m

phi1 = bio.monopole_potential(Io,sigma,r1)
phi2 = bio.monopole_potential(-Io,sigma,r2)
potential = phi1 + phi2 
print r1,r2,sigma,phi1,phi2,potential,"Volts"


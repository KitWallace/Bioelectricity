import bio

print "Frog Muscle" 
frog_muscle = [("K+", +1, 124, 2.2), ("Na+", +1, 4.0, 109.0), ("Cl-",-1, 1.5, 77.0)] # from L2
ion_Vm = bio.Nernst_membrane_equilibrium(frog_muscle)  
print "ion Vms", ion_Vm


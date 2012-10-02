import bio

print "Squid Nerve"
squid_nerve = [("K+",+1, 397.0, 20.0), ("Na+", +1, 50.0, 437.0), ("Cl-",-1, 40.0, 556.0)]
# compute the equilibrium voltage for each ion
ion_Vm = bio.Nernst_membrane_equilibrium(squid_nerve)
print "ion Vms" , ion_Vm
# sum the voltages for each ion (voltage is the second item in the tuple)
Vm = sum ([ ion[1] for ion in ion_Vm])
print "membrane Vm" , Vm


import bio

#  from http://www.bem.fi/book/03/03.htm#01 3.5.2

print "Cat Motorneuron" 
cat = [("K+", +1, 150, 5.5), ("Na+", +1, 15.0, 150), ("Cl-",-1, 9, 125)] 
ion_Vm = bio.Nernst_membrane_equilibrium(cat)  
print "ion Vms", ion_Vm


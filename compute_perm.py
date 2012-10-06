import bio
from solve import monotonic

#  given ion concentrations and membrane potential Vm,
#  find the permeability ratio of Na+ to K+ 
#  consider clorine to be irrelevant

T = 26
Vm = -0.091
membrane = bio.Membrane(
           { "K+" : bio.Ion( +1, 124, 2.2, 1 ),
             "Na+" : bio.Ion( +1, 4.0, 109.0, 1),
             "Cl-":  bio.Ion(-1, 1.5, 77.0, 0) 
           }            
          ) 

def f(x) :
   """ reverse potential is a function of the Na+ permeability """
   membrane.ions["Na+"].permeability = x
   return membrane.reverse_potential(T)   

s = monotonic(f,Vm,0.0,100.0,err=0.0001)
print s

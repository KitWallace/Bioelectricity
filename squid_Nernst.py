import bio
# squid nerve
# Lecture 2 slide 12
T = 20
membrane = bio.Membrane( 
      {   "K+": bio.Ion(+1, 397, 20),
          "Na+": bio.Ion( +1, 50, 437 ),
          "Cl-": bio.Ion(-1, 40, 556 ) 
      }
   )

for ion in membrane.ions.items() :
   print ion[0], "Nerst equilibrium=", ion[1].equilibrium_potential(T)

import bio
# frog muscle
# Lecture 2 slide 12
T = 20
membrane = bio.Membrane(
           { "K+" : bio.Ion( +1, 124, 2.2),
             "Na+" : bio.Ion( +1, 4.0, 109.0),
             "Cl-":  bio.Ion(-1, 1.5, 77.0) 
           }            
          ) 
for ion in membrane.ions.items() :
   print ion[0], "Nerst equilibrium=", ion[1].equilibrium_potential(T)

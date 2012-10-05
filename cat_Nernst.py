import bio
#  cat motorneoron
#  from http://www.bem.fi/book/03/03.htm#01 3.5.2

T = 37.5
membrane = bio.Membrane(
           { "K+" : bio.Ion( +1, 150, 5.5,6.5),
             "Na+" : bio.Ion( +1, 15, 150,1),
             "Cl-":  bio.Ion(-1, 9, 125,20) 
           }            
          ) 
for ion in membrane.ions.items() :
   print ion[0], "Nerst equilibrium=", ion[1].equilibrium_potential(T)

print "reverse potential " , membrane.reverse_potential(T)

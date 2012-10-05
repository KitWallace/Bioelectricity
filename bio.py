import math

#  constants
F =  9.64853365E4         # Faraday  units: C mol-1  source : http://physics.nist.gov/cgi-bin/cuu/Value?f
R =  8.3144621            # Gas constant units: J K-1 mol-1   source: http://physics.nist.gov/cgi-bin/cuu/Value?r
T0 = 273.15               # 0 C units: degrees K  source: http://www1.bipm.org/en/si/si_brochure/chapter2/2-1/2-1-1/kelvin.html

def RToverF(Tc) :
  """ the ratio RT/F is a function of Tc, the temperature in degrees Celcius 
  dimension is V 
  """
  return  R * (T0+ Tc ) / F

def length(p) :
  """ compute the distance between the origin and a point in 3-d space 
  p is a tuble (x, y, z)
  """
  return math.sqrt(p[0]*p[0] + p[1]*p[1] + p[2]*p[2])

def subtract(p1,p2) :
  """ compute the position of p2 relative to p1. Points are expressed as tuples.
  """
  return (p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2])

def monopole_potential(Io,sigma,r) :
  """ compute the potential in volts at a distance r from a monopole current source
  Io current in amp
  sigma  - conductivity in ohm-1 m-1
  r distance in m
  dimensionally  of the equation is amp / (ohm-1 m-1 m)  = amp ohm  = volt
  """
  return Io / (4 * math.pi * sigma *  r )

def dipole_potential(Io,sigma,r,d,theta) :
  """ compute the potential in volts at a distance r angle theta, from a dipole 

  Io current in amp
  sigma  - conductivity in ohm-1 m-1
  r distance in m
  d separation of the dipole m 
  theta angle in radians between point and the axis of the dipole (90 is at right angles to axis of the dipole)
  dimensionally  of the equation is amp m / (ohm-1 m-1 m2)  = amp ohm  = volt
  """
  return Io * d * math.cos(theta) / (4 * math.pi * sigma * r * r)


class Ion(object) :
    """ represents a snge ion on either side of a membrane
    """
    def __init__ (self,valance,internal,external,permeability=0) :
       self.valance = valance
       self.internal_concentration = float(internal)
       self.external_concentration = float(external)
       self.permeability =  float(permeability)

    def equilibrium_potential (self, T = 25) :
       """ based on the Nerst equation
       T is the temperature in degrees Celcius
       see http://www.physiologyweb.com/calculators/nernst_potential_calculator.html
       """
       Vm = ( RToverF(T) / self.valance) * math.log(self.external_concentration / self.internal_concentration)
       return Vm

    def description(self,T) :
       " ".join(("Valance", str(self.valance) ,
            "External Concentration", str(self.external_concentration), "Internal Concentration", str(self.internal_concentration),
            "Permeability",str(self.permeability), "Equilibrium  (20C)= ", str(self.equilibrium_potential(T)),"V"))

class Membrane(object) :
    """ represents a membrane as a dictionary of ions, indexed by their name
    """
    def __init__(self,ions) :
       """ ions is a dictionary of ions with names as indexes
       """
       self.ions = ions

    def reverse_potential (self,T = 25) :
       """ reverse potential for a membrane based on the Goldman-Hodgkin-Katz equation 
       T is the temperature in degrees Celcius
 
       see http://www.physiologyweb.com/calculators/ghk_equation_calculator.html
       """
       pe = sum ( [ ion.permeability * 
                  ( ion.external_concentration if ion.valance > 0 else ion.internal_concentration ) 
                    for ion in self.ions.values() ]) 
       pi = sum ( [ ion.permeability * 
                 ( ion.external_concentration if ion.valance < 0 else ion.internal_concentration ) 
                    for ion in self.ions.values() ]) 
       if (pi == 0) :
          return None
       else :
          Vm = RToverF(T) * math.log (pe/ pi) 
       return Vm



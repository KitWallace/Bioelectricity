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


def Nernst_ion_equilibrium (ion, T = 25) :
   """ ion concentration across a membrane is represented by a tuple (symbol, valance, internal and external concentration )
       symbol eg "K+"
       valance is the sign of the ion 
       internal is the molar concentration of the ion interior to the cell
       exterior is the molar concentration of the ion external to the cell 
       units of concentration are irrelevant since the ratio of concentrations is used but typically expressed in mol m-3
       T is the temperature in degrees Celcius
       return the symbol and the computed Voltage between interior and exterior
   """
   (symbol,valance,internal,external) = ion
   Vm =( RToverF(T) / valance) * math.log(float(external) / float(internal))
   return (symbol,Vm)

def Nernst_membrane_equilibrium (ions,T = 25) :
   """
   ions is a list of ion concentrations 
   return a list of ion potentials 
   """
   return [ Nernst_ion_equilibrium(ion,T) for ion in ions ]


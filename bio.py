import math

def distance(x=0,y=0,z=0) :
  return math.sqrt(x*x + y*y + z*z)

def distanceBetween(p1,p2) :
  return distance(p1[0]-p2[0],p1[1]-p2[1],p1[2]-p2[2])

def monopole_potential(Io,sigma,r) :
  """ compute the potential in volts at a distance r from a monopole current source
  Io current in amp
  sigma  - conductivity in ohm-1 m-1
  r distance in m
  dimensionally  of the equation is amp / (ohm-1 m-1 m)  = amp ohm  = volt
  """
  return Io / (4 * math.pi * sigma *  r )


import math

def length(p) :
  """ compute the distance between the origin and a point in 3-d space 
  p is a tuble (x, y, z)
  """
  return math.sqrt(p[0]*p[0] + p[1]*p[1] + p[2]*p[2])

def subtract(p1,p2) :
  """ compute the position of p2 relative to p1. Points are expressed as tuples.
  """
  return (p1[0]-p2[0],p1[1]-p2[1],p1[2]-p2[2])

def monopole_potential(Io,sigma,r) :
  """ compute the potential in volts at a distance r from a monopole current source
  Io current in amp
  sigma  - conductivity in ohm-1 m-1
  r distance in m
  dimensionally  of the equation is amp / (ohm-1 m-1 m)  = amp ohm  = volt
  """
  return Io / (4 * math.pi * sigma *  r )


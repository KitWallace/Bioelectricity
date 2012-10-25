
import copy,math

class Membrane (object) :
    def __init__(self, Vm, n, m, h, dt) :

# week 4 / slide 38
        #  fixed variables
        self.Cm = 1  #   membrane capacitance 1 micro farad / cm 2
        # voltages in millivolts
		
	self.ENa =  52.4    # Ernst Potential for sodium ions
	self.EK  = -72.1    # Ernst potential for potassium ions
	self.EL =  -49.2    #  Leakage potential
	self.VR   = -60     # resting membrane potential
        #  conductance in micro Siemans / cm2 
        self.GNa_max  = 120 # maximum Na channel conductance  
        self.GK_max  = 36 # maximum K channel conductance
        self.GL_max  = 0.3 # maximum L channel conductance

	# state variables
        self.Vm =  Vm   # in millvolts
	self.n  = n     # sodium channel particles
        self.m  = m     # potassium channel particle 1
        self.h  = h     # potassium channel particle 2
        self.dt = dt    # in milliseconds
        self.t = 0.0
        self.Istim = 0   # stimulus current = 0

# week 4 / slide 12  and slide 55
    @property    
    def IIon (self) :
	return self.INa + self.IK + self.IL

    @property    
    def dVm(self) :
	return self.dt * (self.Istim - self.IIon) / self.Cm
 				
# week 4 /slide 17
    @property
    def IK (self) :
	return self.GK * (self.Vm - self.EK)
	
    @property
    def GK (self) :
	return  self.GK_max * pow(self.n,4)

# week 4 /slide 19
    @property
    def INa (self) :
	return self.GNa * (self.Vm - self.ENa)		
 
    @property
    def GNa (self) :	
        return  self.GNa_max * pow(self.m,3) * self.h
    
# week 4 /slide 21
    @property
    def IL (self) :
	return self.GL * (self.Vm - self.EL)
		
    @property
    def GL (self) :	
        return  self.GL_max     

# week 4 / slide 24-25   
    @property 
    def dn (self) :
        return self.dt * (self.alpha_n * (1.0 - self.n) + self.beta_n * self.n) 

    @property 
    def dm (self) :
	return self.dt * (self.alpha_m * (1.0 - self.m) + self.beta_m * self.m)
	
    @property 
    def dh (self) :
	return self.dt * (self.alpha_h * (1.0 - self.h) + self.beta_h * self.h)

# week 4 / slide 28-29
    @property 
    def vm(self) :
        return self.Vm - self.VR
		

# week 4 /slide 35  - simplified
    @property
    def alpha_n(self) :	
        if abs(10 - self.vm) > 1.E-7 :
	    an = 0.01 * (10.0 - self.vm)/(math.exp((10-self.vm)/10) - 1)
        else :
     	    an = 0.1
	return an
		
    @property
    def beta_n(self) :
	return 0.125 * math.exp(-self.vm/80)

# week 4 /slide 36  - simplified
    @property
    def alpha_m(self) :	
	if abs(25.0-self.vm)  > 1.E-7 :
            am=0.1*(25.0-self.vm) / (math.exp((25-self.vm)/10) - 1)
        else :
            am = 1.0
	return am

    @property
    def beta_m(self) :
	return  4.0 * math.exp(-self.vm/18)

# week 4 /slide 37  
    @property
    def alpha_h(self) :
	return 0.07 * math.exp(-self.vm/20)
		
    @property
    def beta_h(self) :
	return 1.0  /(math.exp((30-self.vm)/10)+1)

    def step(self) :
# make a copy of all the membrane data
        new = copy.copy(self)  
# increment the state variables
        new.n = self.n + self.dn
        new.m = self.m + self.dm
        new.h = self.h + self.dh
        new.Vm = self.Vm + self.dVm
        new.t = self.t + self.dt
        return new	

# print all variable values by inspecting the object's dictionary	
    def show(self) :
        print 'State at time', self.t
        for name in dir(self):
           attr = getattr(self,name)
           if not callable(attr) and not (name[0:2] == "__"):
              print name,':',attr

# set 1 with no stimulus current 
# week 4 / slide 38
squid= Membrane(Vm=-11.5, n=0.378, m=0.417, h=0.477, dt=50E-3)
squid.show()
squid= squid.step()
squid.show()




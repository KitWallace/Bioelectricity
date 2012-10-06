def monotonic(f, Y , low , high, err=0.001, max=20) :
   """ solve f(x) = Y where f is a monotonically increasing or decreasing function of x 
   low is the initial lower bound on x - float
   high is the initial upper bound on x - float
   err is the required precision of the solution - float
   max is the maixium number of iterations if convergence to err fails - int
 
   returns the value of x which solves f(x) = Y or None if no convergence
   """ 
   n = 0
   while True :
     n+= 1
     if n > max :
        return None
     flow = f(low)
     fhigh = f(high)
     x = (low + high) / 2
     fx = f(x)
#     print low, flow, high, fhigh, x, fx
     if  abs(fx-Y) < err :
        return x
     else :
        if fx < Y :
           if flow < fhigh :
              low = x
           else :
              high = x
        else :
           if flow < fhigh :
              high = x
           else :
              low = x
    
if __name__ == "__main__" :
   def f(x) : 
      """ monotonicly increasing """ 
      return  (x * x) 

   s = monotonic(f, 2.0, 0.0, 10.0, 0.01)
   print s 

   def f2(x) : 
      """ monotonicly decreasing """ 
      return - (x * x) 

   s = monotonic(f2, -2.0, -0.0, -10.0, 0.01)
   print s 

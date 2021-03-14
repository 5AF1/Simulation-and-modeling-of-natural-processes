import numpy as np
import math

class Integrator:
    def __init__(self, xMin, xMax, N):
        ################################
        self.dt = (xMax-xMin)/N
        self.xMax = xMax
        self.xMin = xMin
        self.N = N
        self.ans = self.integrate()

    def f(self,x):
        e = math.e
        return x**2 * e**(-x) * np.sin(x)

    def rectify(self,i):
        return self.xMin+i*self.dt

    def integrate(self):       
        ##################################
        val = np.fromfunction(lambda i, j: self.f(self.rectify(j))*self.dt ,(1,self.N))
        return np.sum(val)


    def show(self):
        ##################################
        print(self.ans)

        

examp = Integrator(1,3,200)
#examp.integrate()
examp.show()
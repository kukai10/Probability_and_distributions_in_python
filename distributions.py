import matplotlib.pyplot as plt
import numpy as np

class uniform_dis:
    def __init__(self, a=0, b=1):
        if b < a: a, b = b, a
        self.a = a
        self.b = b
    
    def __setAB__(self, a, b):
        self.__setA__(a)
        self.__setB__(b)
        self.__updateVal__()

    def __setA__(self, a):
        self.a = a
    def __setB__(self, b):
        self.b = b

    def __updateVal__(self):
        self.pdf = self.__pdf__
        self.cdf = self.__cdf__
        self.mean = self.b-self.a 
        self.median = (self.b-self.a) / 2
        self.var = (self.b-self.a)**2 / 12
        self.skewness = 0
        self.kurtosis = 9/5
        
    def __sample__(self, number_of_samples):
        pass

    def __pdf__(self): 
        return [(0, "for x < {}".format(self.a)), 
                (1/(self.b-self.a) , "for {0} <= x <= {1}".format(self.a, self.b)),
                (0, "for x > {}".format(self.b))]

    def __cdf__(self):
        return [(0,  "for x < {}".format(self.a)),
                ("x-{0} / x-{1}", "for {0} <= x <= {1}".format(self.a, self.b)),
                (0, "for x > {}".format(self.b))]

class normal_dis:
    pass

class lognormal_dis:
    pass

class poisson:
    pass
class gamma_dis:
    pass
class exp_dis:
    pass
class geometric_dis:
    pass
class hypergeometric_dis:
    pass

class bernoulli_dis:
    pass
class binomial_dis:
    pass

x = uniform_dis()
x.__setAB__(10, 80)
"""
    This is for all the public parameters used in the programs.
"""
import numpy as np
import cmath
import random
import cmath


det = 0.1               #delta sign
rabi = 0                #omega sign
Gamma = 0.1 * rabi      #Gamma sign
h = 6.626e-34           #planck constant
hbar = h/2/np.pi
m = 9.11e-31            #mass of a electron
hat = np.matrix([[1, 0],
                 [0, 1]])
prob = np.array([3, 7]) #[a,b] represent for a/(a+b) with [1,0] and b/(a+b) with [0,1]
delt = 0
heff = hbar/2*np.matrix([[det, rabi],
                         [rabi, -det-(0+1j)*Gamma]])
init = np.matrix([[0],
                  [1]])
jump = np.sqrt(Gamma/2) * np.matrix([[0,1],
                                     [0,0]])

#random value defined
def random_value():
    random.seed(376940)
    x = random.random()
    return x



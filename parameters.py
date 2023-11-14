"""
    This is for all the public parameters used in the programs.
"""
import numpy as np

a, b = 1, 0
det = 0        #delta sign
rabi = 1                #omega sign
Gamma = 0.1 * rabi      #Gamma sign
h = 6.626e-34           #planck constant

delt = (1 / 100) * (1 / rabi) * (2 * np.pi)
time = 1000 * delt # unis: s
prob = np.matrix([[a],
                  [b]]) #[a,b] represent for a/(a+b) with [1,0] and b/(a+b) with [0,1]
prob1 = np.array([a,b])

heff = 1/2*np.matrix([[det, rabi],
                         [rabi, -det-(0+1j)*Gamma]])
init = np.matrix([[1],
                  [0]])
jump = np.sqrt(Gamma/2) * np.matrix([[0,1],
                                     [0,0]])

#random value defined





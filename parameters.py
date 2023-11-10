"""
    This is for all the public parameters used in the programs.
"""
import numpy as np

a, b = 1, 0
det = 1              #delta sign
rabi = 10                #omega sign
Gamma = 0.1 * rabi      #Gamma sign
h = 6.626e-34           #planck constant
hbar = h/2/np.pi
time = 10 # unis: s
delt = 0.01
hat = np.matrix([[1, 0], [0, 1]])
prob = np.matrix([[a],
                  [b]]) #[a,b] represent for a/(a+b) with [1,0] and b/(a+b) with [0,1]
prob1 = np.array([a,b])

heff = 1/2*np.matrix([[det, rabi],
                         [rabi, -det-(0+1j)*Gamma]])
init = np.matrix([[0],
                  [1]])
jump = np.sqrt(Gamma/2) * np.matrix([[0,1],
                                     [0,0]])

#random value defined





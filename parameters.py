"""
    This is for all the public parameters used in the programs.
"""
import numpy as np

#for single particle
a, b = 1, 0
det = -0.8                 #delta sign
rabi = 1                #omega sign
Gamma = 0.1      #Gamma sign
h = 6.626e-34           #planck constant

delt = (1 / 200) * (1 / rabi)
#delt = 0.002
#iteration = 10000
#time = iteration * delt # unis: s
time = 50
iteration = int(time/delt)
prob = np.matrix([[a],
                  [b]]) #[a,b] represent for a/(a+b) with [1,0] and b/(a+b) with [0,1]
prob1 = np.array([a,b])

heff = 1/2*np.matrix([[det, rabi],
                         [rabi, -det-(0+1j)*Gamma]])
init = np.matrix([[1],
                  [0]])
jump = np.sqrt(Gamma/2) * np.matrix([[0,1],
                                     [0,0]])

#for 2 time correlation
chi_plus = [1,0]
chi_mines = [1,0]





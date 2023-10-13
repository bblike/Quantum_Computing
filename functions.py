"""
    THis file is for the definition of all the function used in the main program.
"""
import numpy as np
import parameters as paras
import random

def trial(x):
    return x + 1

"""
    new ideas: use /phi as parameters and take Hhat as the function calculation.
"""
#test function
def func1(phi):
    return paras.hat*phi#just a idea how the function works, not working indeed.

#density matrix caculation
def density_matrix(phi):
    a = phi[0]
    b = phi[1]
    density = [[a, 0], [0, b]]
    return density

#transpose function calculation
def tri(phi):
    trimat = np.transpose(phi)
    return trimat

#one time revolution at time t
def revolution(phi, t):
    density = density_matrix(phi)
    result = (1 - cmath.i/)

#generate of random value between 0 and 1
def random_value():
    random.seed(376940)
    x = random.random()
    return x

def norm_squared(phi):
    result = 0

    return result


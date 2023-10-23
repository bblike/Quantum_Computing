"""
    THis file is for the definition of all the function used in the main program.
"""
import numpy as np
import parameters as paras
import decimal


"""
    new ideas: use /phi as parameters and take Hhat as the function calculation.
"""
#test function
def func1(phi):
    return paras.hat*phi#just a idea how the function works, not working indeed.

#density matrix caculation
def density_matrix(prob):
    a = prob[0]
    b = prob[1]
    sum = a + b
    a = a / sum
    b = b / sum
    density = [[a, 0], [0, b]]
    return density


#one time revolution at time t
def evolution(phi, t):
    print("h=", paras.h)
    print("heff=", paras.heff)
    print("delt=", paras.delt)
    print("phi=", phi)
    next = (1 - (0+1j)/paras.h*paras.heff * paras.delt) * phi
    return next

#compare r with inner products
def comparison(function, r):
    print("function=", function)
    print("r=", r)
    innerproduct = inner(function)
    print("inner product =", innerproduct)
    if r < innerproduct:
        result = function / np.sqrt(innerproduct)
    else:
        result = daga(function)/np.sqrt(inner(daga(function)))
    return result

def norm_squared(phi):
    norm = np.linalg.norm(phi)
    return phi/norm

def inner(phi):
    inner_product = np.vdot(np.conj(phi), phi)
    return inner_product

def daga(function):
    result = paras.jump * function
    return result


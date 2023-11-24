"""
    THis file is for the definition of all the function used in the main program.
"""
import numpy as np
import parameters as paras


# one time revolution at time t
def evolution(phi, t):

    inter_step = (np.matrix([[1,0],[0,1]]) - (0+1j)*paras.heff * t)
    next_step = inter_step * phi
    return next_step


# compare r with inner products
def comparison(function, r, flag):

    innerproduct = np.abs(inner(function))
    # print(innerproduct)
    if r < innerproduct:
        # print("Jump failed")
        result = function / np.sqrt(innerproduct)
        #flag = flag + 1
    else:
        # print("Jump succeed")
        #result = jump(function) / np.sqrt(inner(jump(function)))
        result = np.matrix([[1], [0]])  # use of daga calculation give the same method but lose precision
        # for the time between collapse
        #flag = 0
    temp = np.abs(np.conj(result[1])*result[1])
    flag = temp
    # print(temp)
    return result, temp, flag


# calculate inner product
def inner(phi):
    inner_product = phi[0]*np.conj(phi[0])+phi[1]*np.conj(phi[1])
    return inner_product


# jump of the function
def jump(function):
    result = paras.jump * function
    return result


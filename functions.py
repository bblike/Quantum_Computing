"""
    THis file is for the definition of all the function used in the main program.
"""
import numpy as np
import parameters as paras



#density matrix caculation
def density_matrix(prob):
    [[a],[b]] = prob
    sum = a**2 + b**2
    density = [[a**2/sum, 0], [0, b**2/sum]]
    return density


#one time revolution at time t
def evolution(phi, t):

    #print("h=", paras.h)
    #print("heff=", paras.heff)
    #print("delt=", paras.delt)
    #print("phi=", phi)

    inter = (np.matrix([[1,0],[0,1]]) - (0+1j)*paras.heff * paras.delt)
    #print("inter = ", inter)
    next = inter * phi
    return next

#compare r with inner products
def comparison(function, r, flag):

    #print("function=", function)
    #print("r=", r)
    innerproduct = inner(function)
    #print("inner product =", innerproduct)

    if r < innerproduct:
        #print("Jump failed")

        result = function / np.sqrt(innerproduct)
    else:
        #print("Jump succeed")

        if flag == 0:
            flag = 1
        elif flag == 1:
            flag = 0

        result = np.matrix([[1],[0]])
    temp = np.abs(np.conj(result[1])*result[1])

    #print(temp)
    return result, temp, flag


def inner(phi):
    inner_product = phi[0]*np.conj(phi[0])+phi[1]*np.conj(phi[1])
    return inner_product

def daga(function):
    result = paras.jump * function
    return result


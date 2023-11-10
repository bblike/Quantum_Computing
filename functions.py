"""
    THis file is for the definition of all the function used in the main program.
"""
import numpy as np
import parameters as paras
import scipy
import decimal



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
    temp = []
    #print("function=", function)
    print("r=", r)
    innerproduct = inner(function)
    print("inner product =", innerproduct)
    if r < innerproduct:
        print("Jump failed")
        temp.append(0)
        result = function / np.sqrt(innerproduct)
    else:
        print("Jump succeed")
        temp.append(1)
        if flag == 0:
            flag = 1
        elif flag == 1:
            flag = 0
        result = daga(function)/np.sqrt(inner(daga(function)))

    return result, temp, flag
def inner_compare(x,y):
    a = x.real
    b = x.imag
    c = y.real
    d = y.imag

    if a**2+b**2 < c**2+d**2:
        return True
    else:
        return False


def record(phi):

    [[top],
     [bot]]=phi
    top = np.abs(top)

    return top

def inner(phi):
    inner_product = np.abs(np.vdot(np.conj(phi), phi))
    return inner_product

def daga(function):
    result = paras.jump * function
    return result


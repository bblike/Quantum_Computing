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

    inter = (np.matrix([[1,0],[0,1]]) - (0+1j)/paras.hbar*paras.heff * paras.delt)
    #print("inter = ", inter)
    next = inter * phi
    return next

#compare r with inner products
def comparison(function, r):
    temp = []
    #print("function=", function)
    #print("r=", r)
    innerproduct = inner(function)
    #print("inner product =", innerproduct)
    if inner_compare(r, innerproduct):
        #print("Jump failed")
        temp = [0]
        result = function / np.sqrt(innerproduct)
    else:
        #print("Jump succeed")
        temp = [1]
        result = daga(function)/np.sqrt(inner(daga(function)))
    return result, temp
def inner_compare(x,y):
    a = x.real
    b = x.imag
    c = y.real
    d = y.imag

    if a**2+b**2 < c**2+d**2:
        return True
    else:
        return False


def normalisation(phi):
    [[top],
     [bot]]=phi
    """
    treal = top.real
    timag = top.imag
    breal = bot.real
    bimag = bot.imag
    t = np.sqrt(treal**2+timag**2)
    b = np.sqrt(breal**2+bimag**2)
    total = np.sqrt(treal**2+timag**2+breal**2+bimag**2)
    print(total)
    phi[0][0] = np.real(t/total)
    phi[1][0] = np.real(b/total)"""
    top = np.abs(top)
    bot = np.abs(bot)
    total = np.sqrt(top**2+bot**2)
    top = top / total
    bot = bot / total
    phi[0][0] = top
    phi[1][0] = bot
    return phi

def inner(phi):
    inner_product = np.vdot(np.conj(phi), phi)
    return inner_product

def daga(function):
    result = paras.jump * function
    return result


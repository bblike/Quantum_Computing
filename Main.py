print("Hello world!")
"""
    This program is for the task in computing project.
    The goal of this program is to simulate particles with behaviors represented by Monte Carlo wave function.
    Compare this with OBE mode to see the differences.
    
"""
#import matplotlib.pyplot as plt
import functions as func
import parameters as paras
import random
import numpy as np
import matplotlib.pyplot as plt
import time
random.seed(384756)




#this is the beginning of matrix
print("The initial states are probability = ", paras.prob)
x = func.density_matrix(paras.prob)
print("which gives the density function: ", x)
y = paras.prob
y1 = paras.prob1
print("the original state is:", y)


def one_complete_evolution(func1, func2):
    function = np.matrix([[func1],[func2]])
    print("doing the first revolution")
    result1 = func.evolution(function, paras.delt)
    print("result1 = ", result1)

    print("doing the first comparison")
    r = random.random()

    flag = func.comparison(result1, r)
    print("flag=", flag)

    print("renormalisation")
    normed_result = func.normalisation(flag)
    print("results = ", normed_result)
    return normed_result

def one_particle():
    paras.sucounter = []
    funcs = np.array(y1)
    print(type(funcs))
    print("funcs = ", funcs[1])
    result = []
    for i in range(0, 1000):
        if i == 0:
            result = one_complete_evolution(funcs[i], funcs[i+1])
        if i > 0:
            #print(funcs[0][i])
            result = one_complete_evolution(funcs[0][i], funcs[1][i])
        #print(result)
        result1 = np.array(result)
        #print("funcs = ", funcs)
        #print("result1 = ", result1)
        funcs = np.c_[funcs, result1]
        #print("new funcs is", funcs)
        print("evolution {} finished.".format(i))
        print("***********************************")

    print(paras.sucounter)
    return paras.sucounter

finals = []
for i in range(1, 10):
    x = one_particle()
    if finals == []:
        finals = x
    else:
        for m in range(0, len(x)):
            finals[m] = finals[m] + x[m]
    print("{} particle calculation done.".format(i))
    print("finals = ", finals)
    time.sleep(0.5)

for i in range(0, len(finals)):
    finals[i] = sum(finals[i])

plt.figure()
plt.plot(np.array(range(0, 1000)), finals)
plt.show()


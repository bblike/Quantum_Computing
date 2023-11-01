#print("Hello world!")
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
import multiprocessing as mp
random.seed(384756)

# this is the beginning of matrix
#print("The initial states are probability = ", paras.prob)
x = func.density_matrix(paras.prob)
#print("which gives the density function: ", x)
y = paras.prob
y1 = paras.prob1
#print("the original state is:", y)
finals = []
n_cpu = 4


def one_complete_evolution(func1, func2):
    function = np.matrix([[func1],[func2]])
    #print("doing the first revolution")
    result1 = func.evolution(function, paras.delt)
    #print("result1 = ", result1)

    #print("doing the first comparison")
    r = random.random()

    flag, counter = func.comparison(result1, r)
    #print("flag=", flag)

    #print("renormalisation")
    normed_result = func.normalisation(flag)
    #print("results = ", normed_result)
    return normed_result, counter

def one_particle():
    sucounter = []
    flag = []
    funcs = np.array(y1)
    #print(type(funcs))
    #print("funcs = ", funcs[1])
    result = []
    for i in range(0, 1000):
        if i == 0:
            result, flag = one_complete_evolution(funcs[i], funcs[i+1])
        if i > 0:
            #print(funcs[0][i])
            result, flag = one_complete_evolution(funcs[0][i], funcs[1][i])
        #print(result)
        result1 = np.array(result)
        sucounter.append(flag)
        #print("funcs = ", funcs)
        #print("result1 = ", result1)
        funcs = np.c_[funcs, result1]
        #print("new funcs is", funcs)
        #print("evolution {} finished.".format(i))
        #print("***********************************")

    #print(sucounter)
    return sucounter

def task(q,n, l):
    res = []

    for k in n:
        for i in k:
            re = one_particle()
            #print(re)
            #print("{} finished".format(i))
            if res == []:
                res = re
            else:
                for j in range(len(res)):
                    res[j] = res[j] + re[j]
            print("job {} finished".format(i))
    #print("res = ", res)
    q.put(res)

def parallel():
    l=mp.Lock()
    q = mp.Queue()
    total = 1000
    procs = []
    ret = []
    chunk_size = int(total / n_cpu)
    print("Number of used: ", n_cpu)
    #distribute tasks
    for i in range(0, n_cpu):
        min_i = chunk_size * i

        if i < n_cpu-1:
            max_i = chunk_size * (i+1)
        else:
            max_i = total
        digits = []
        for digit in range(min_i, max_i):
            digits.append(digit)
        #print(digits)
        #print(len(digits))
        procs.append(mp.Process(target=task, args=(q, [digits], l)))
    for proc in procs:
        proc.start()
    res = []
    for proc in procs:
        while proc.is_alive():
            while False == q.empty():
                res.append(q.get())
    for proc in procs:
        proc.join()
    print("1")



    print(res)
    return res
if __name__ == '__main__':

    finals = parallel()
    print("program done")
    plot = np.array(finals[0]) + np.array(finals[1])
    plot1 = np.zeros(len(plot))
    for i in range(len(plot)):
        plot1[i] = np.sum(plot[i])
    print(plot1)
    plt.figure()
    plt.plot(np.array(range(len(plot1))), plot1)
    plt.show()


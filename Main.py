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
#random.seed(384756)

# this is the beginning of matrix
#print("The initial states are probability = ", paras.prob)
x = func.density_matrix(paras.prob)
#print("which gives the density function: ", x)
y1 = paras.prob1
#print("the original state is:", y)
finals = []
n_cpu = 6
n_particle = 1000

def one_complete_evolution(func1, func2, flag):
    tracing = []
    function = np.matrix([[func1], [func2]])
    #print("doing the first revolution")

    result1 = func.evolution(function, paras.delt)
    #print("result1 = ", result1)
    temp = func.record(result1)
    #print("doing the first comparison")
    r = random.random()

    result, traced, flag = func.comparison(result1, r, flag)
    tracing.append(traced)
    #record the value


    print("unnormaled=", result)
    #print("normaled = ", normed_result)
    return result, temp, flag #result is the function, tracing is bool in 1/0 represent success or not

def one_particle():
    sucounter = []
    flag = 0
    flag_tracing = [0]
    funcs = np.array(y1)
    tracing1 = []
    #print(type(funcs))
    #print("funcs = ", funcs[1])
    result = []
    result1 = []
    for i in range(0, int(paras.time/paras.delt)):
        if i == 0:
            result, tracing, flag = one_complete_evolution(funcs[i], funcs[i+1], flag)
        if i > 0:
            #print(funcs[0][i])
            result, tracing, flag = one_complete_evolution(funcs[0][i], funcs[1][i], flag)
        #print(result)
        result1 = np.array(result)
        tracing1.append(np.array(tracing))
        flag_tracing.append(flag)
        #sucounter.append(flag)
        #print("funcs = ", funcs)
        #print("result1 = ", result1)
        funcs = np.c_[funcs, result1]
        #print("new funcs is", funcs)
        #print("evolution {} finished.".format(i))
        #print("***********************************")

    #print(sucounter)
    #print(sucounter)
    return funcs, tracing1, flag_tracing

def task(q,n, l):
    res = []
    flags = []
    for k in n:
        for i in k:
            function, re, flag= one_particle()
            #print(re)
            #print("{} finished".format(i))
            if res == []:
                res = re
                flags = flag
            else:
                for j in range(len(res)):
                    res[j] = res[j] + re[j]
                    flags[j] = flags[j] + flag[j]
            print("job {} finished".format(i))
    #print("res = ", res)
    q.put(flags)

def parallel():
    l = mp.Lock()
    q = mp.Queue()
    total = n_particle
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

    return res

def unpack(a):
    new_list = []
    for element in a:
        new_list.append(element[0])
    return new_list

def plot_flag(x):
    new_list = []
    for element in x:
        if new_list != []:
            for i in range(len(new_list)):
                new_list[i] += np.array(element[i])
        else:
            new_list = element
    return np.array(new_list)


if __name__ == '__main__':

    finals = parallel()
    print("program done")
    #print(finals)
    #print(len(finals[n_cpu-1]))

    #single tracing
    """ 
    plot = np.array(finals[0])
    for i in range(2):
        plot = unpack(plot)
    plot1 = np.zeros(len(plot))

    print(plot)
    a = plt.figure()
    plt.plot(np.array(range(len(plot)))*paras.delt, plot)

    """
    #multiple tracing
    print(finals)
    """plot1 = np.zeros(int(paras.time/paras.delt))
    for element in finals:
        temp_plot = np.array(element)
        for i in range(2):
            plot = unpack(temp_plot)
            for j in range(len(plot)):
                plot1[j] += int(plot[j])"""
    plot1 = plot_flag(finals)
    print(plot1)
    #plot the graph
    a = plt.figure()
    xs = np.array(range(len(plot1)))*paras.delt
    ys = plot1/n_particle
    plt.plot(xs[:-1], ys[:-1])
    plt.title("multiple")
    plt.ylim([0,1])
    plt.ylabel("Population")
    plt.xlabel("time")
    plt.show()
    a.savefig("multiple_particle_trajectory1.png")

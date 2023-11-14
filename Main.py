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
from tqdm import tqdm
#random.seed(384756)


# this is the beginning of matrix
#print("The initial states are probability = ", paras.prob)
x = func.density_matrix(paras.prob)
#print("which gives the density function: ", x)
y1 = paras.prob1
#print("the original state is:", y)
finals = []
n_cpu = 8
n_particle = 1000
total_task = int(n_particle*paras.time/paras.delt)
current_task = 0


def update():
    global current_task
    pre = 0
    current = 0
    current_task = current_task + 1
    print("current_task=", current_task)
    current = int(current_task*100/total_task)
    if current != pre:
        print("{}% finished.".format(current))



def one_complete_evolution(func1, func2, flag):
    tracing = []
    function = np.matrix([[func1], [func2]])
    #print("doing the first revolution")

    result1 = func.evolution(function, paras.delt)
    #print("result1 = ", result1)

    #print("doing the first comparison")
    r = random.random()
    temp = 0
    result, traced, flag = func.comparison(result1, r, flag)
    tracing.append(traced)
    #record the value


    #print("unnormaled=", result)
    #print("normaled = ", normed_result)
    return result, traced, flag #result is the function, tracing is bool in 1/0 represent success or not

def one_particle():
    global current_task
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

    update()
    return funcs, tracing1, flag_tracing

def task(q,n, l):
    res = []
    flags = []
    current = 0
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

    #print("res = ", res)
    q.put([res, flags])

def parallel():
    l = mp.Lock()
    q = mp.Queue()
    total = n_particle
    procs = []
    ret = []
    chunk_size = int(total / n_cpu)
    print("Number of used: ", n_cpu)
    print("total task number: ", total_task)
    print("estimated time: ", total_task/n_cpu/13625, "s")
    begin=time.time()
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
    end=time.time()
    print("time spent = {}s".format(end-begin))

    return res, end

def unpack(a):
    new_list = []
    for element in a:
        new_list.append(element)
    return np.array(new_list)

def plot_flag(x):
    new_list = []
    for element in x:
        if new_list != []:
            for i in range(len(new_list)):
                new_list[i] += np.array(element[i])
        else:
            new_list = element
    return np.array(new_list)

def diff(a,b):
    result = []
    for i in range(len(a)):
        if a[i] == 0:
            result.append(0)
        else:
            result.append((a[i]-b[i])/b[i])

    return result

if __name__ == '__main__':

    final, times = parallel()
    finals = []
    finals2 = []
    for element in final:
        finals.append(element[0])
        finals2.append(element[1])
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
    #print(finals)
    """plot1 = np.zeros(int(paras.time/paras.delt))
    for element in finals:
        temp_plot = np.array(element)
        for i in range(2):
            plot = unpack(temp_plot)
            for j in range(len(plot)):
                plot1[j] += int(plot[j])"""



    plot = plot_flag(finals)
    plot1 = np.squeeze(plot)
    #print(plot1)
    #plot the graph




    # Analytical method
    anapop = []
    sinecoef = (3 * paras.Gamma) / np.sqrt(16 * paras.rabi ** 2 - paras.Gamma ** 2)
    frontfactor = (paras.rabi ** 2) / (2 * (paras.rabi ** 2) + paras.Gamma ** 2)


    for t in range(int(paras.time/paras.delt)):
        bothcoef = (np.exp(-3 * paras.Gamma * t * paras.delt / 4))
        argument = np.sqrt(paras.rabi ** 2 - paras.Gamma ** 2 / 16) * t * paras.delt
        r11ana = frontfactor * (1 - bothcoef * (np.cos(argument) + sinecoef * np.sin(argument)))
        anapop.append(r11ana)


    a = plt.figure()
    fig, ax = plt.subplots(2, 1, figsize = [16,9], gridspec_kw={'height_ratios': [3, 1]}, sharex = True)
    xs = np.array(range(len(plot1)))
    ys = plot1/n_particle

    ax[0].plot(range(int(paras.time/paras.delt)), anapop, label='Analytic', color='green')
    ax[0].plot(xs[:-1], ys[:-1], label='Monte Carlo', color='blue')

    ax[0].legend()
    diffplot = diff(anapop[:-1], ys[:-1])
    ax[1].plot(xs[20:-1], diffplot[20:])
    ax[1].legend()

    yline = np.zeros(len(xs[:-1]))
    yline += 0.01
    ax[1].plot(xs[20:-1], yline[20:])
    yline -= 0.02
    ax[1].plot(xs[20:-1], yline[20:])
    plt.show()

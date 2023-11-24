# print("Hello world!")
"""
    This program is for the task in computing project.
    The goal of this program is to simulate particles with behaviors represented by Monte Carlo wave function.
    Compare this with OBE mode to see the differences.
    
"""

import functions as func
import parameters as paras
import random
import numpy as np
import matplotlib.pyplot as plt
import time
import multiprocessing as mp

# random.seed(384756)
y1 = paras.prob1
finals = []
n_cpu = 6
n_particle = 1000
total_task = int(n_particle * paras.time / paras.delt)
current_task = 0
wow = r"""

                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |# '.
                 / \\|||  :  |||# \
                / _||||| -:- |||||- \
               |   | \\\  -  #/ |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               佛祖保佑         永无BUG
            Buddha bless no bug forever
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

def one_complete_evolution(func1, func2, flag):  # function used for one evolution

    tracing = []
    function = np.matrix([[func1], [func2]])
    result1 = func.evolution(function, paras.delt)
    r = random.random()
    result, traced, flag = func.comparison(result1, r, flag)
    tracing.append(traced)
    return result, traced, flag  # result is the function, tracing is bool in 1/0 represent success or not


def one_particle():  # function for a particle in the whole time period
    flag = []
    flag_tracing = []
    funcs = np.array(y1)
    tracing1 = []
    tracing = []
    result = []
    for i in range(0, int(paras.time / paras.delt)):
        if i == 0:
            result, tracing, flag = one_complete_evolution(funcs[i], funcs[i + 1], flag)
        if i > 0:
            result, tracing, flag = one_complete_evolution(funcs[0][i], funcs[1][i], flag)

        result1 = np.array(result)
        tracing1.append(np.array(tracing))
        flag_tracing.append(flag)
        funcs = np.c_[funcs, result1]

    return funcs, tracing1, flag_tracing


def task(q, n):
    res = []
    flags = []

    for k in n:
        for i in k:
            function, re, flag = one_particle()

            if not flags:
                res = re
                flags = flag
            else:
                for j in range(len(res)):
                    res[j] = res[j] + re[j]
                    #flags[j] = flags[j] + flag[j]

    # print("res = ", res)
    q.put([res, flags])


def parallel():  # multi core processing

    q = mp.Queue()
    total = n_particle
    procs = []

    chunk_size = int(total / n_cpu)
    print("Number of Core used: ", n_cpu)
    print("total task number: ", total_task)
    print("estimated time: ", total_task / n_cpu / 10000, "s")
    begin = time.time()
    # distribute tasks
    for i in range(0, n_cpu):
        min_i = chunk_size * i

        if i < n_cpu - 1:
            max_i = chunk_size * (i + 1)
        else:
            max_i = total
        digits = []
        for digit in range(min_i, max_i):
            digits.append(digit)
        # print(digits)
        # print(len(digits))
        procs.append(mp.Process(target=task, args=(q, [digits])))
    for proc in procs:
        proc.start()
    res = []
    for proc in procs:
        while proc.is_alive():
            while False == q.empty():
                res.append(q.get())
    for proc in procs:
        proc.join()
    end = time.time()
    print("time spent = {}s".format(end - begin))

    return res, end


def unpack(a):  # change the type of result
    new_list = []
    for element in a:
        new_list.append(element)
    return np.array(new_list)


def plot_flag(x):
    new_list = []
    for element1 in x:
        if new_list != []:
            for i in range(len(new_list)):
                new_list[i] += np.array(element1[i])
        else:
            new_list = element1
    return np.array(new_list)


def diff(a, b):  # calculate the percentage difference
    result = []
    for i in range(len(a)):
        if a[i] == 0:
            result.append(0)
        else:
            # result.append((a[i] - b[i]) / a[i])
            result.append(a[i] - b[i])

    return result


if __name__ == '__main__':
    print(wow)
    final, times = parallel()
    finals = []
    finals2 = []
    for element in final:
        finals.append(element[0])
        finals2.append(element[1])
    print("program done")

    plot = plot_flag(finals)
    plot1 = np.squeeze(plot)

    # Analytical method
    anapop = []
    sinecoef = (3 * paras.Gamma) / np.sqrt(16 * paras.rabi ** 2 - paras.Gamma ** 2)
    frontfactor = (paras.rabi ** 2) / (2 * (paras.rabi ** 2) + paras.Gamma ** 2)

    for t in range(int(paras.time / paras.delt)):
        bothcoef = (np.exp(-3 * paras.Gamma * t * paras.delt / 4))
        argument = np.sqrt(paras.rabi ** 2 - paras.Gamma ** 2 / 16) * t * paras.delt
        r11ana = frontfactor * (1 - bothcoef * (np.cos(argument) + sinecoef * np.sin(argument)))
        anapop.append(r11ana)

    # plot the graph
    plt.figure()
    fig, ax = plt.subplots(2, 1, figsize=[16, 10], gridspec_kw={'height_ratios': [4, 1]}, sharex=True)
    xs = np.array(range(len(plot1)))
    ys = plot1 / n_particle

    ax[0].plot(range(int(paras.time / paras.delt)), anapop, label='OBE Analytic', color='green')
    ax[0].plot(xs[:-1], ys[:-1], label='Monte Carlo', color='blue')

    ax[0].legend()
    diffplot = diff(anapop[:-1], ys[:-1])
    ax[1].plot(xs[20:-1], diffplot[20:])


    yline = np.zeros(len(xs[:-1]))
    yline += 0.01
    ax[1].plot(xs[20:-1], yline[20:])
    yline -= 0.02
    ax[1].plot(xs[20:-1], yline[20:])
    ax[0].set_title("Evolution", size=30)
    ax[0].set_ylabel("Population", size=15)
    ax[1].set_title("Difference", size=30)
    ax[1].set_xlabel("Time steps", size=15)
    ax[1].set_ylabel("Percentage", size=15)
    fig.savefig("t={}s,n_particle={}.png".format(round(paras.time, 1), n_particle))
    fig.show()


    # plot the collapse time against time
    new1 = finals2[0]
    new = np.ravel(new1)
    length = len(new)
    xs = range(length)
    xs = np.array(xs)/paras.delt/1000
    fig1 = plt.figure()
    print(len(xs))
    print(len(new))
    plt.plot(xs, np.array(new))
    plt.title("{}".format(round(paras.time, 1)))
    plt.savefig("SingleTracing.png")
    plt.show()

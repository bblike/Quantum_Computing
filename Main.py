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





#this is the beginning of matrix
print("The initial states are probability = ", paras.prob)
x = func.density_matrix(paras.prob)
print("which gives the density function: ", x)
y = paras.init
print("the original state is:", y)
print("doing the first revolution")
result1 = func.evolution(y, paras.delt)
print("result1 = ", result1)
print("doing the first comparison")
print(func.norm_squared(result1))
flag = func.comparison(result1, random.random())
print("flag=", flag)



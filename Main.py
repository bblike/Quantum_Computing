print("Hello world!")
"""
    This program is for the task in computing project.
    The goal of this program is to simulate particles with behaviors represented by Monte Carlo wave function.
    Compare this with OBE mode to see the differences.
    
"""
#import matplotlib.pyplot as plt
import functions as func
import parameters as para
import numpy as np


x = 3
x = func.trial(x)
print(x)
print(para.hat)
test = func.func1(para.phi)
print(test)

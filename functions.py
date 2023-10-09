"""
    THis file is for the definition of all the function used in the main program.
"""
import numpy as np
import parameters as paras

def trial(x):
    return x + 1

"""
    new ideas: use /phi as parameters and take Hhat as the function calculation.
"""

def func1(phi):
    return paras.Hhat*phi#just a idea how the function works, not working indeed.
    

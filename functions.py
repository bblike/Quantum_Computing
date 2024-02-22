"""
    THis file is for the definition of all the function used in the main program.
"""
import numpy as np
import parameters as paras
import xlwt
import xlrd
from xlutils.copy import copy

path = r"C:\Users\Li Zhejun\Desktop\Quantum_Computing\results\result.xls"


# one time revolution at time t
def evolution(phi, t):
    inter_step = (np.matrix([[1, 0], [0, 1]]) - (0 + 1j) * paras.heff * t)
    next_step = inter_step * phi
    return next_step

def two_time_evolution(phi, t):
    chi_plus = (np.matrix)

# compare r with inner products
def comparison(function, r, flag):
    innerproduct = np.abs(inner(function))
    # print(innerproduct)
    if r < innerproduct:
        # print("Jump failed")
        result = function / np.sqrt(innerproduct)

        # flag = flag + 1
    else:
        # print("Jump succeed")
        # result = jump(function) / np.sqrt(inner(jump(function)))
        result = np.matrix([[1], [0]])  # use of daga calculation give the same method but lose precision
        # for the time between collapse
        # flag = 0
    temp = np.abs(np.conj(result[1]) * result[1])
    flag = temp
    # print(temp)
    return result, temp, flag


# calculate inner product
def inner(phi):
    inner_product = phi[0] * np.conj(phi[0]) + phi[1] * np.conj(phi[1])
    return inner_product


# jump of the function
def jump(function):
    result = paras.jump * function
    return result


def writearray(array1, array2):
    terms = []
    numbers = []

    for i in range(len(array1)):
        terms.append(array1[i])
        numbers.append(array2[i])

    terms.append("Detuning")
    numbers.append(paras.det)
    terms.append("Rabi frequency")
    numbers.append(paras.rabi)
    terms.append("Gamma")
    numbers.append(paras.Gamma)
    terms.append("time steps")
    numbers.append(paras.delt)
    terms.append("iteration")
    numbers.append(paras.iteration)
    terms.append("total time")
    numbers.append(paras.time)
    terms.append("jump operator")
    numbers.append(paras.jump)

    return terms, numbers


def excelgenerator(array1, array2):
    assert len(array1) == len(array2)
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('parameters')
    ws.write(1, 1, 'terms')
    ws.write(1, 2, 'number')
    for i in range(len(array1)):
        print(array1[i])
        print(type(array1[i]))
        ws.write(i + 2, 1, array1[i])
        print(array2[i])
        print(type(array2[i]))
        ws.write(i + 2, 2, '{}'.format(array2[i]))

    wb.save("{}.xls".format(array2[1][-4:-1]))


def write_excel_xls_add_sheet(sheet_name, array1, array2):
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    new_workbook = copy(workbook)
    new_worksheet = new_workbook.get_sheet(0)
    add_sheets = new_workbook.add_sheet(sheet_name)
    add_sheets.write(1, 1, 'terms')
    add_sheets.write(1, 2, 'numbers')
    for i in range(len(array1)):
        print(array1[i])
        print(type(array1[i]))
        add_sheets.write(i + 2, 1, array1[i])
        print(array2[i])
        print(type(array2[i]))
        add_sheets.write(i + 2, 2, '{}'.format(array2[i]))

    new_workbook.save(path)

import xlwt
import numpy
import xlrd
from xlutils.copy import copy

path = r"C:\Users\Li Zhejun\Desktop\Quantum_Computing\results"

workbook = xlrd.open_workbook(r"{}\result.xls".format(path)) # get workbook
sheets = workbook.sheet_names() # get worksheet
number = len(sheets) # get total number of worksheet

new_workbook = copy(workbook) # copy to new workbook
new_sheet = new_workbook.get_sheet(0) # name a new sheet
for i in range(number):
    worksheet = workbook.sheet_by_name(sheets[i-1]) # get selected sheet
    rows = worksheet.nrows
    for j in range(rows):
        temp = worksheet.cell_value(j, 2)
        new_sheet.write(j, 3+i, temp)

new_workbook.save(r"{}\result.xls".format(path))
print("write finish")
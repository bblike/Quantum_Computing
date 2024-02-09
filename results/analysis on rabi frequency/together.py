import xlwt
import numpy
import xlrd
from xlutils.copy import copy
from datetime import datetime

path = r"C:\Users\Li Zhejun\Desktop\Quantum_Computing\results\analysis on rabi frequency"

f = open("text.txt", "w")
now = datetime.now()
nowstr = now.strftime("%Y%m%d%H%M%S")
f.write(nowstr)
f.write("\n")
f.close()

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
        if j < rows-1:
            f = open("text.txt", "a")
            f.write(str(temp))# append data in the file
            f.write("\t")
            f.close()
    f = open("text.txt", "a")
    f.write("\n")
    f.close()
new_workbook.save(r"{}\result.xls".format(path))
print("write finish")


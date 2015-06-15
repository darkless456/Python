# excel2.py

import xlrd

def print_xls(path):
    xlsFile = xlrd.open_workbook(path)
    try:
        mySheet = xlsFile.sheets()[0] # 访问第1张表序号0 // xlsFile.sheet_by_name('sheetName') 通过工作表名访问
    except:
        print('no such sheet in file')
        return

    print('%d rows, %d cols' % (mySheet.nrows, mySheet.ncols)) # 输出工作表共几行（rows）和几列（cols）


    for row in range(0, mySheet.nrows):
        temp = ''
        for col in range(0, mySheet.ncols):
            if mySheet.cell(row, col).value != None:
                temp += str(mySheet.cell(row, col).value) + '\t'
        print(temp)

if __name__ == '__main__':
    print_xls('D:\\python_path\\sample_ex.xls')
'''
模块是对象，并且所有的模块都有一个内置属性 __name__。一个模块的 __name__ 的值取决于您如何应用模块。如果 import 一个模块，
那么模块__name__ 的值通常为模块文件名，不带路径或者文件扩展名。但是您也可以像一个标准的程序样直接运行模块，在这种情况下,
__name__ 的值将是一个特别缺省"__main__"。

在cmd 中直接运行.py文件,则__name__的值是'__main__';

而在import 一个.py文件后,__name__的值就不是'__main__'了;

从而用if __name__ == '__main__'来判断是否是在直接运行该.py文件
'''

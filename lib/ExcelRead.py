#!/usr/bin/env python
# -*- coding: utf-8 -*-

#需要先安装xlrd: pip install xlrd

import xlrd


class read_excel(object):
    def __init__(self, excel_path):
        #excel_path为excel文件的路径及名称
        self.data = xlrd.open_workbook(excel_path)

    def sheet_name_list(self):
        sheet_name_list = self.data.sheet_names()
        return sheet_name_list

    def excel_nrows(self, sheet_num):
        self.tablen = self.data.sheet_by_index(sheet_num)
            # 得到某个工作表，或者通过索引顺序或工作表名称
            # table1 = self.data.sheets()[sheet_num]
            # table1 = self.data.sheet_by_name('sheet1')
        self.nrows = self.tablen.nrows
        # 获取行数
        return self.nrows

    def excel_ncols(self,sheet_num):
        self.tablen = self.data.sheet_by_index(sheet_num)
        self.ncols = self.tablen.ncols
        # 获取列数
        return self.ncols

    def rows_in_excel(self, sheet_num):
        for i in range(self.excel_nrows(sheet_num)):
            print "row %s : %s" % (i, self.tablen.row_values(i))

    def one_row_value(self, row_num):
        return self.tablen.row_values(row_num)

    def one_col_value(self, col_num):
        return self.tablen.col_values(col_num)

    def cols_in_excel(self, sheet_num):
        for j in range(self.excel_ncols(sheet_num)):
            print "col %s : %s" % (j, self.tablen.ncols(j))

    def cell_in_excel(self, a, b):
        cell_xn = self.tablen.cell(a, b).value
        # 或者使用行列索引：
        # cell_xn= table1.row(0)[0].value
        # cell_xn=table1.col(1)[0].value
        return cell_xn


# 获取整行和整列的值（数组）
# print self.table1.row_values(0)
# print self.table1.col_values(0)

if __name__ == '__main__':
    #获取data.xlsx文件中第0号sheet的内容
    readex = read_excel('D:\SYProject\data.xlsx')
    print '该Excel表中sheet名称列表为：%s' % readex.sheet_name_list()
    print '第0号sheet中共有%s行，%s列' % (readex.excel_nrows(0), readex.excel_ncols(0))
    print '第0号sheet中的所有行：'
    readex.rows_in_excel(0)

    print '单元格(1,1)的内容为：%s' % (readex.cell_in_excel(1, 1))
    print '第一行的内容为：%s' % (readex.one_row_value(1))
    print '第一列的内容为：%s' % (readex.one_col_value(1))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd


def read_excel(excel_path):
    # excel_path = excel文件路径
    data = xlrd.open_workbook(excel_path)
    table1 = data.sheets()[0]
    nrows = table1.nrows

    for i in range(nrows):
        print "row %s: %s" % (i, table1.row_values(i))

if __name__ == '__main__':
    read_excel()
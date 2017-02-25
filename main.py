#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import logging
import unittest
from lib.Logger import Logger
from lib.HTMLTestRunner import HTMLTestRunner



if __name__ == '__main__':
    logger = Logger().getlog()
    logger.info('测试开始...')

    #生成HTML格式的测试报告
    report_path = './result/test_result_%s.html' % time.strftime(("%Y -%M-%D %H-%M-%S"))
    fp = open(report_path,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'XXX测试报告',
                            description=u'测试用例执行情况：')
    runner.run(suite())
    fp.close()






    logger.info('测试结束。')


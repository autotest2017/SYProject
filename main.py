#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import logging
import unittest
import sys
# sys.path.append('.\\lib\\Logger.py')
# sys.path.append('.\\lib\\HTMLTestRunner.py')
from lib.Logger import Logger
from lib.HTMLTestRunner import HTMLTestRunner
from testcase.admin_login_logout.admin_login_correction import AdminLoginCorrection
from testcase.admin_login_logout.admin_login_failure import AdminLoginFail
from lib.sendmail import send_email
from config import *


def suite():
    u"""创建测试套"""
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromTestCase(AdminLoginCorrection))
    test_suite.addTests(loader.loadTestsFromTestCase(AdminLoginFail))
    return test_suite


if __name__ == '__main__':
    logger = Logger().getlog()
    logger.info(u'测试开始...')

    #生成HTML格式的测试报告
    report_path = './result/test_result_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S")
    fp = open(report_path,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'XXX测试报告',
                            description=u'测试用例执行情况：')
    runner.run(suite())
    fp.close()
    send_email(FROM_ADDR, FROM_PSWD, TO_ADDR, u"测试报告模版", report_path, mode="html")
    logger.info(u'测试结束。')


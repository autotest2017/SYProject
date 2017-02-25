#!/usr/bin/env python
#encoding:utf-8

import os
import time
import logging

class Logger(object):#object是所有类的基类
    def __init__(self, logname='./log/logger.log',loglevel=logging.DEBUG):
        """
            定义初始化函数。
            两个参数logname和loglevel都配置了默认值。
            logname定义了输出日志的路径和名称
            loglevel=logging.DEBUG 表明级别高于DEBUG的日志内容都输出

        怎么设置log日志的路径在当前路径上一级路径中的某个目录？
       """

        # 创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(loglevel)

        #创建一个handler,用于写入日志文件
        fh = logging.FileHandler(logname)
        fh.setLevel(loglevel)

        #再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(loglevel)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d  - %(message)s')
        fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(fmt)

        #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return  self.logger

    """
        为什么不直接定义一个函数，实现上面Init中的内容？
    """

if __name__ == '__main__':
    logger = Logger("product.log", logging.DEBUG).getlog()
    logger.info('info message')
    logger.error("error message")
    logger.warn("warn message")
    logger.critical("critical message")
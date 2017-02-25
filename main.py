#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import logging
import unittest
from lib.Logger import Logger


if __name__ == '__main__':
    logger = Logger().getlog()
    logger.info('测试开始...')
    logger.info('测试结束。')


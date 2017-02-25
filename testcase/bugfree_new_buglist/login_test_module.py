#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coder: samren
# version : 1.0
import unittest


class UTExample1(unittest.TestCase):
    def test_minus(self):
        """测试减法"""
        self.assertEqual(2 - 1, 1)
        print "minus"

    def test_add_sum(self):
        """测试加法"""
        #1.做了一些操作
        a, b= 1, 1
        #2.把预期结果与实际结果作比较，从而判断是否成功
        self.assertEqual(2, a+b)
        print "add_sum"
        #self.assertTrue(False, "这里应该为True")
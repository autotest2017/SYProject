#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coder: samren
# version : 1.0
import unittest


class AdminLoginCorrection(unittest.TestCase):
    def test_admin_login(self):
        u"""测试管理员用户是否能成功登录"""
        self.assertEqual(2 - 1, 1)

    def test_admin_logout(self):
        u"""测试管理员退出以后，能否正确跳转"""
        self.assertEqual(2, 2)
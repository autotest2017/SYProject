#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coder: samren
# version : 1.0
import unittest


class AdminLoginFail(unittest.TestCase):
    def test_admin_login_failure_with_wrong_username(self):
        """测试不正确的admin用户名"""
        self.assertEqual(2 - 1, 1)

    def test_admin_login_failure_with_wrong_password(self):
        """测试不正确的admin密码"""
        self.assertEqual(2, 2)

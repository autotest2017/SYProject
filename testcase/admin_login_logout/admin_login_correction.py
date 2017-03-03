#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coder: samren
# version : 1.0
import unittest
from selenium import webdriver


class AdminLoginCorrection(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_admin_login(self):
        u"""测试管理员用户是否能成功登录"""
        sdr = self.driver
        sdr.get(self.base_url + 'bugfree/')
        sdr.find_element_by_id('LoginForm_username').clear()
        sdr.find_element_by_id('LoginForm_username').send_keys('admin')
        sdr.find_element_by_id('LoginForm_password').clear()
        sdr.find_element_by_id('LoginForm_password').send_keys('123456')
        sdr.find_element_by_id('SubmitLoginBTN').click()
        self.assertEqual('BugFree', sdr.title)

    def test_admin_welcome_content(self):
        u"""测试管理员登录后，欢迎信息是否正确"""
        sdr = self.driver
        sdr.get(self.base_url + 'bugfree')
        sdr.find_element_by_id('LoginForm_username').clear()
        sdr.find_element_by_id('LoginForm_username').send_keys('admin')
        sdr.find_element_by_id('LoginForm_password').clear()
        sdr.find_element_by_id('LoginForm_password').send_keys('123456')
        sdr.find_element_by_id('SubmitLoginBTN').click()
        self.assertRegexpMatches(sdr.find_element_by_css_selector("BODY").text, r"^[\s\S]*欢迎,  系统管理员 | [\s\S]*$")

    def test_admin_logout(self):
        u"""测试管理员退出以后，能否正确跳转"""
        sdr = self.driver
        sdr.get(self.base_url + 'bugfree')
        sdr.find_element_by_id('LoginForm_username').clear()
        sdr.find_element_by_id('LoginForm_username').send_keys('admin')
        sdr.find_element_by_id('LoginForm_password').clear()
        sdr.find_element_by_id('LoginForm_password').send_keys('123456')
        sdr.find_element_by_id('SubmitLoginBTN').click()
        sdr.find_element_by_partial_link_text(u'退出').click()
        self.assertEqual(u'登录 - BugFree', sdr.title)


if __name__ == '__main__':
    unittest.main()
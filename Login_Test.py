#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver


class BugfreeLoginLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_login_needpsw(self):
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("admin")
        driver.find_element_by_id("SubmitLoginBTN").click()
        self.assertEqual(u"密码 不可为空白.", driver.find_element_by_id("login-error-div").text)

    def test_login_NoUser(self):
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("a")
        driver.find_element_by_id("LoginForm_password").send_keys("123456")
        driver.find_element_by_id("SubmitLoginBTN").click()
        self.assertEqual(u"用户名不存在", driver.find_element_by_id("login-error-div").text)

    def test_login_sucess(self):
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("123456")
        driver.find_element_by_id("SubmitLoginBTN").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'标题2')])[2]").click()
        driver.find_element_by_link_text(u"退出").click()
    

if __name__ == "__main__":
    unittest.main()

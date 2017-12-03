import unittest

import time

from day6.database.connectDb import connDb
from diwutian.myTestCase import myTestCase


class ZhuCeTest(myTestCase):
    def test_Zhu_Ce(self):
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element_by_name("username").send_keys("aicaiying")
        driver.find_element_by_name("password").send_keys("111111")
        driver.find_element_by_name("userpassword2").send_keys("111111")
        driver.find_element_by_name("mobile_phone").send_keys("15001234567")
        driver.find_element_by_name("email").send_keys("54654@qq.com")
        driver.find_element_by_class_name("reg_btn").click()
    #检查数据库中新增加的用户名和我们输入的是否一致。
        expected="aicaiying"
        time.sleep(5)
        actual=connDb()[1]
        self.assertEqual(expected,actual)

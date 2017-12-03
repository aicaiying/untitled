import unittest

import time
from selenium import webdriver

class MemberManageTest(unittest.TestCase):
    def setUp(self):
        # 打开浏览器.变量前面加上self表示这个变量是类的属性
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

# driver声明在setUp方法之内，不能被其他方法访问
    def tearDown(self):
        time.sleep(20)
        self.driver.quit()

    def test_add_number(self):
        self.driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        self.driver.find_element_by_name("username").send_keys("admin")
        self.driver.find_element_by_name("userpass").send_keys("password")
        self.driver.find_element_by_name("userverify").send_keys("1234")
        self.driver.find_element_by_name("userverify").submit()
        self.driver.find_element_by_link_text("会员管理").click()
        self.driver.find_element_by_link_text("添加会员").click()
        frame=self.driver.find_element_by_css_selector("#mainFrame")
        self.driver.switch_to.frame(frame)
        time.sleep(5)
        self.driver.find_element_by_name("username").clear()
        self.driver.find_element_by_name("username").send_keys("meimei")
        self.driver.find_element_by_name("mobile_phone").clear()
        self.driver.find_element_by_name("mobile_phone").send_keys("15695925841")
        self.driver.find_element_by_css_selector("[value='0']").click()
        self.driver.find_element_by_name("birthday").clear()
        self.driver.find_element_by_name("birthday").send_keys("19901212")
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys("js@qq.com")
        self.driver.find_element_by_name("qq").clear()
        self.driver.find_element_by_name("qq").send_keys("123456")
        self.driver.find_element_by_css_selector("body > div.content > div.install.mt10 > dl > dd > div > div > dl > form > dd > div > input").click()


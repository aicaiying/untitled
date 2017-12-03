import csv
import os
import unittest

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MemberManageTest(unittest.TestCase):

    # 在当前类只执行一次
    @classmethod
    def setUpClass(cls):
        print("所有方法之前,执行一次")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.quit()

    def read(file_name):
        # 所有的重复代码的出现，都是程序设计的不合理
        # 重复的代码应该封装到一个方法里
        current_file_path = os.path.dirname(__file__)
        path = current_file_path.replace("Day4", "data/" + file_name)
        print(path)
        # file=open(path,'r')
        # 因为文件一关闭，里面的数据也随着消失，所以单独声明一个列表来保存里面的数据
        result = []
        # with语句是一个代码块，代码块中的内容都要缩进4个空格,with代码块可以自动关闭with中中声明的变量file
        with open(path, 'r') as file:
            data_table = csv.reader(file)
            for row in data_table:
                result.append(row)
        return result
    def testa_log_in(self):
        print("登录测试 ")
        driver = self.driver
        driver.get("http://localhost/admin.php")
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234").send_keys(Keys.ENTER).perform()

    def testb_add_member(self):
        print("添加会员")
        driver = self.driver
        for row in read("member_info.csv"):
            driver.find_element_by_link_text("会员管理").click()
            driver.find_element_by_link_text("添加会员").click()
                # driver.switch_to.frame("mainFrame")
                # 如果frame没有name属性时, 我们可以通过其他方式定位iframe标签, 把定位好的页面元素传给driver.switch_to.frame(iframe_html)方法也可以实现frame切换
            iframe_css = "#mainFrame"
            iframe_html =driver.find_element_by_css_selector(iframe_css)
            driver.switch_to.frame(iframe_html)
            driver.find_element_by_name("username").send_keys("row[0]")


if __name__ == '__main__':
    unittest.main()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day6.page_object.login_page import LoginPage
from day6.page_object.personalCebterpage import PersonalCenterPage
from diwutian.myTestCase import myTestCase

class LoginTest(myTestCase):
    def test_login(self):
      #   1.打开网页
        #self.driver.get("http://localhost/index.php?m=user&c=public&a=login")
        lp=LoginPage(self.driver)
        lp.open()
        #2.输入用户名

        lp.input_username("caiying")
        #self.driver.find_element(By.ID,"username").send_keys("caiying")
        #self.driver.find_element(By.ID,"password").send_keys("111111")
        #self.driver.find_element(By.CLASS_NAME,"login_btn").click()
        #3.输入密码
        lp.input_password("111111")
        #4.点击登陆按钮
        lp.click_loginbutton()
        #5.验证是否跳转到管理中心页面
        #expected="我的会员中心 - 道e坊商城 - Powered by Haidao"
        time.sleep(5)
        pcp=PersonalCenterPage(self.driver)
        self.assertEqual(pcp.title,self.driver.title)


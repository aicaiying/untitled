
import  unittest
from selenium import webdriver

class myTestCase(unittest.TestCase):
    def setUp(self):
        #打开浏览器
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  #浏览器的版本和driver的版本必须匹配才能用窗口最大化在selenium官网上找

    def testDown(self):
        self.driver.quit()



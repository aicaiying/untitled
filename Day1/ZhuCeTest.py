#有了myTestCase以后，再写测试用例，就不需要重新写setUp和tearDown
import os


from diwutian.myTestCase import myTestCase

class ZhuCeTest (myTestCase):
    #因为MyTestCase已经实现了setUp和tearDown方法，我们以后在写测试用例就不需要重新实现setUp和tearDown方法
    def test_zhe_ce(self):
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        actual=driver.title
        expected="用户注册 - 道e坊商城 - Powered by Haidao"
        base_path=os.path.dirname(__file__)
        path=base_path.replace('diwutian','report/image/')
        driver.get_screenshot_as_file(path+"zhuce.png")
        #截取整个浏览器的图片
        self.assertEqual(actual,expected)

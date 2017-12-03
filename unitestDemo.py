#测试框架是干啥用的
import unittest

class UntestDemo(unittest.TestCase):
            # 重写父类中的方法setUp
            # def是方法的关键字
            def setUp(self):
                print("这个方法将会在测试案例执行前先执行")
            def tearDown(self):
                print("这个方法将会在测试用例方法之后执行")
            def test_denglu(self):
                print("登陆测试用例")
                self.zhu_ce()
            def zhu_ce(self):
                print("注册测试用例")
            def test_search(self):
                print("收索测试用例")
if __name__ == '__main__':
    unittest.main()




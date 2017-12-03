import unittest


if __name__ == '__main__':
#首字母大写说明他是一个类，类不能直接调用方法，必须实例化，python中实例化不需要new 关键字
    suite=unittest.defaultTestLoader.discover('./diwutian', pattern='*Test.py')
    unittest.TextTestRunner().run(suite)


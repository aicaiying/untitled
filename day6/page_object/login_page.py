#构造方法的作用
#实例化LoginPage对象的时候，需要把driver作为参数传进来
#便于别的属性和方法使用driver
from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self,driver):
        self.driver=driver
    title="用户登录 - 道e坊商城 - Powered by Haidao"
    url="http://localhost/index.php?m=user&c=public&a=login"
    user_input_loc=(By.ID,"username")
    #小括号是元组，元组中两个元素，第一个元素是控件的定位方式
    #第二个元素，控件定位方式的具体的值
    password_input_loc=(By.ID,"password")
    click_loginbutto_loc=(By.CLASS_NAME,"login_btn")
    expected = "我的会员中心 - 道e坊商城 - Powered by Haidao"
    def open(self):
        self.driver.get(self.url)
#前面加个*表示的是传入的不是元组而是元组中的两个元素
    def input_username(self,username):
        self.driver.find_element(*self.user_input_loc).send_keys(username)

    def input_password(self,password):
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    def click_loginbutton(self):
        self.driver.find_element(*self.click_loginbutto_loc).click()


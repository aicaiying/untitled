#登陆
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("yichao")
ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()
driver.find_element_by_link_text("账号设置").click()
driver.find_element_by_partial_link_text("个人资料").click()
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("龙行天和")
driver.find_element_by_css_selector("[value='2']").click()
#javascript不能在pharcharm中执行
js='document.getElementById("date").removeAttribute("readonly")'
driver.execute_script(js)
driver.find_element_by_id("date").clear()
#clac = driver.find_element_by_id("date")
#driver.execute_script('arguments[0].removeAttribute("readonly")', date)
driver.find_element_by_id("date").send_keys("20170405")
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("9522255212")
driver.find_element_by_class_name("btn4").click()
time.sleep(3)
driver.switch_to.alert.accept()

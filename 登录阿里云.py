#coding=utf-8
import os,re,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Firefox()

driver.get("https://signin.aliyun.com/1753746924904024.onaliyun.com/login.htm?callback=https%3A%2F%2Fhome.console.aliyun.com%2Fnew")
time.sleep(2)
username_input = driver.find_element_by_id("user_principal_name")
time.sleep(2)
username_input.send_keys(Keys.CONTROL,'a')
username_input.send_keys(Keys.BACK_SPACE)
username_input.send_keys("live_zwq@1530764968739604.onaliyun.com",Keys.RETURN)


time.sleep(2)
password_input = driver.find_element_by_id("password_ims")
time.sleep(2)
password_input.send_keys("Br912912")
time.sleep(2)
password_input.send_keys(Keys.RETURN)
#20s, 手动填入动态码
time.sleep(20)
driver.get("https://hbr.console.aliyun.com/#/cloud/hana?_k=test")

#悬停在regions上面
region = driver.find_element_by_xpath("//div[@id='hbr']/a[0]")
region_act = ActionChains(driver).move_to_element(region).perform()
print(type(region_act))
print(region_act)
shanghai = driver.find_element_by_id("cn-shanghai")
shanghai.click()

time.sleep(3)

#hana = driver.find_element_by_elementSAP HANA备份
#找到log In 按钮
#logon = driver.find_element(By.XPATH, '//button[text()="Log In"]')
#点击登录 这个时候跳到了登录页面
#logon.click()

#打开system Information的界面
#sysinfo = driver.find_element_by_id("tabset_sysInfo")
#sysinfo.click()

#获取summary信息
#health_table = driver.find_element_by_id("healthSummaryTable")
#获取所有的row
#rows = health_table.find_elements(By.TAG_NAME, "tr")
#for row in rows:
  #获取列信息, col是个<span>元素
#  col = row.find_elements(By.TAG_NAME, "td")[1]
  #打印<span>元素的text信息
#  print col.text

#获取其中单个硬件信息，比如 点击Fan
#其他的复制Fan的信息攫取代码

time.sleep(30)
#driver.quit()

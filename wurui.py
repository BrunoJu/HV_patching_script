#coding=utf-8
import os,re,time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


#让浏览器记住密码，使用profile登录
f=open('profile_directory.txt','r')
s=f.readlines()
#修改这个的profile路径
#profile_directory = r'C:\Users\c5258641\AppData\Roaming\Mozilla\Firefox\Profiles\7870jpat.default'
profile_directory=s[1]
profile = webdriver.FirefoxProfile(profile_directory)
driver = webdriver.Firefox(profile)

#打开iLO登录页面，修改内容
driver.get("https://gmp.wdf.sap.corp/")
#找到log In 按钮
#logon = driver.find_element(By.XPATH, '//button[text()="Log In"]')
#点击登录 这个时候跳到了登录页面
#logon.click()

#打开system Information的界面
sysinfo = driver.find_element_by_id("tabset_sysInfo")
sysinfo.click()

#获取summary信息
health_table = driver.find_element_by_id("healthSummaryTable")
#获取所有的row
rows = health_table.find_elements(By.TAG_NAME, "tr")
for row in rows:
  #获取列信息, col是个<span>元素
  col = row.find_elements(By.TAG_NAME, "td")[1]
  #打印<span>元素的text信息
  print col.text

#获取其中单个硬件信息，比如 点击Fan
#其他的复制Fan的信息攫取代码

driver.quit()

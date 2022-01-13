'''
pip install selenium
驱动下载地址https://sites.google.com/a/chromium.org/chromedriver/downloads
下载后把驱动文件加入环境变量。或者直接把驱动文件和 Python脚本放到同一文件夹下面
'''

from lib2to3.pgen2 import driver
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('www.baidu.com')

## 获取元素
driver.find_element_by_id("id")
driver.find_element_by_name("name")

## xpath路径的方式来获取元素
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
search_input = driver.find_element_by_id("kw") # 获取到百度搜索框
search_input.send_keys("刘亦菲")  # 自动输入 刘亦菲
submit = driver.find_element_by_id("su")  # 获取到百度一下按钮
submit.click()  # 点击搜索


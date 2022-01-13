'''
pip install selenium
驱动下载地址https://sites.google.com/a/chromium.org/chromedriver/downloads
下载后把驱动文件加入环境变量。或者直接把驱动文件和 Python脚本放到同一文件夹下面
'''

from lib2to3.pgen2 import driver
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('www.baidu.com')

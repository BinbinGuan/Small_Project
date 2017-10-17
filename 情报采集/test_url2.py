#-*- coding:utf-8 -*-
import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


f = open("/home/xuna/桌面/res/韦小宝工作室.txt",'w')
sum = 1
url = "http://www.yiduoxiaohua.com/"
driver = webdriver.Chrome()
driver.set_window_size(400,400) #设置浏览器窗口的大小
driver.get(url)

for n in range(3,41):#2-21
    #//*[@id="goods"]/table/tbody/tr[3]/td[1]
    #//*[@id="goods"]/table/tbody/tr[5]/td[1]
    #//*[@id="goods"]/table/tbody/tr[6]/td[1]
    #//*[@id="goods"]/table/tbody/tr[11]/td[1]
    #//*[@id="goods"]/table/tbody/tr[40]/td[1]
    try:
        title = driver.find_element_by_xpath('//*[@id="goods"]/table/tbody/tr[' + str(n) + ']/td[1]').text
        price = driver.find_element_by_xpath('//*[@id="goods"]/table/tbody/tr[' + str(n) + ']/td[2]').text
        stock = driver.find_element_by_xpath('//*[@id="goods"]/table/tbody/tr[' + str(n) + ']/td[3]').text

        tmp_str = title + "_&_" + price + "_&_" + stock + "\n"
        f.write(tmp_str + "\n")
        print sum,title,price,stock

    except:
        pass
    sum = sum + 1
driver.close()

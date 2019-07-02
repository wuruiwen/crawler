# -*- coding: utf-8 -*-
"""

"""
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import datetime
import codecs
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

url='http://icp.chinaz.com/provinces/%E5%B1%B1%E8%A5%BF/30'

url1='http://icp.chinaz.com/provinces?&companytype=&city=%u5C71%u897F&custype=0&companyName=&page='
page=1
driver = webdriver.Firefox()
driver.set_page_load_timeout(50)
driver.maximize_window()
for i in range(10):
    url=url1+str(page)
    driver.get(url)
    driver.implicitly_wait(10)
html = driver.page_source
print(html)

driver.get(url1)
driver.implicitly_wait(10)
html1 = driver.page_source
print(html1)


result_table= driver.find_element_by_name('result_table')
print(result_table)


next_page=driver.find_element_by_name()
driver.find_elements_by_xpath("//a[@onclick=]")
<a onclick="m.page.goto(2)">2</a>

driver.find_elements_by_xpath("//div[@id='pagelist']")
driver.find_element_by_xpath('//div[@id="pagelist"]/a/@onclick')

n=2
page = "m.page.goto("+str(n)+")"
driver.find_element_by_xpath("//div[@id='pagelist']/a/[@onclick='"+page+"']")
driver.find_element_by_xpath("//div[@id='pagelist']/a/[@onclick='m.page.goto(2)']")

driver.find_element_by_xpath("//div[@id='pagelist']/a[2]")
ele_fromDate = driver.find_element_by_id('fromDate')
ele_toDate = driver.find_element_by_id('toDate')
ele_search = driver.find_element_by_class_name('search-btn')
ele_toCity.clear()
ele_toCity.send_keys('太原')
ele_toCity.click()
ele_fromDate.clear()
ele_fromDate.send_keys(today)
ele_toDate.clear()
ele_toDate.send_keys(tomorrow)
ele_search.click()
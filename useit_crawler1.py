# -*- coding: utf-8 -*-
"""

"""
from bs4 import BeautifulSoup
#from lxml import html
import xml
import requests
import re
import pandas as pd
import time
import urllib.request
import urllib.parse
import re
import os
import time

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import datetime
import codecs



url0='https://www.useit.com.cn/forum-352-'
url='https://www.useit.com.cn/forum-352-1.html'

page=1
driver = webdriver.Firefox()
driver.set_page_load_timeout(50)
driver.maximize_window()

driver.get(url)
driver.implicitly_wait(10)
html = driver.page_source
print(html)
page_amount=driver.find_element_by_xpath("/span[@id='fd_page_top']")
print(page_amount)
''' for i in range(10):
    url=url1+str(page)
    driver.get(url)
    driver.implicitly_wait(10)
html = driver.page_source
print(html)
 '''
''' driver.get(url1)
driver.implicitly_wait(10)
html1 = driver.page_source
print(html1)

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
ele_search.click() '''
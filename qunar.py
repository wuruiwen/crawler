##医院爬虫

from bs4 import BeautifulSoup
from lxml import html
import xml
import requests
import re
import pandas as pd

def get_soup(url):
 page=requests.get(url)
 soup=BeautifulSoup(page.content, "lxml") 
 return soup

url = 'https://yyk.99.com.cn/shanxi/'
soup=get_soup(url)

df = pd.DataFrame(columns = ["hospital_name", "address", "phone"])

df1 = pd.DataFrame()

for p in soup.find_all("table"):
 for p1 in p.find_all("a",href=True):
  hospital_page='https://yyk.99.com.cn'+p1['href']
  hospital_name=p1['title']
  p2=get_soup(hospital_page)
  p3=p2.find("div",attrs={"class": "wrap-info"})
  p4=p3.find_all("p")
  phone=p4[2].find("em").get_text()
  address=p4[3].find("em").get_text()
  df=df.append([[hospital_name,address,phone]])

df.to_csv("hospital_list.csv",  encoding='utf_8_sig')

df.columns = ["hospital_name", "address", "phone"]





# -*- coding: utf-8 -*-
"""

"""
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import datetime
import codecs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class QunaSpider(object):
    def get_hotel(self,driver,to_city,fromdate,todate):
        ele_toCity = driver.find_element_by_name('toCity')
        ele_fromDate = driver.find_element_by_id('fromDate')
        ele_toDate = driver.find_element_by_id('toDate')
        ele_search = driver.find_element_by_class_name('search-btn')
        ele_toCity.clear()
        ele_toCity.send_keys(to_city)
        ele_toCity.click()
        ele_fromDate.clear()
        ele_fromDate.send_keys(fromdate)
        ele_toDate.clear()
        ele_toDate.send_keys(todate)
        ele_search.click()
        page_num = 0
        while True:
            try:
                WebDriverWait(driver,10).until(
                        EC.title_contains(str(to_city))
                        )
            except Exception as e:
                print (e)
                break
            time.sleep(5)
            js = "window.scrollTo(0, document.body.scrollHeight);"
            driver.execute_script(js)
            time.sleep(5)
            htm_const = driver.page_source
            soup = BeautifulSoup(htm_const,'html.parser',from_encoding='utf-8')
            infos = soup.find_all(class_="item_hotel_info")
            f = codecs.open(str(to_city)+str(fromdate)+u'.html','a+')
            for info in infos:
                f.write(str(page_num)+'--'*50)
                content = info.get_text().replace(" ","").replace("\t","").strip()
                for line in [ln for ln in content.splitlines()if ln.strip()]:
                    f.write(line)
                    f.write('\r\n')
                f.close()
                try:
                    next_page = WebDriverWait(driver,10).until(
                    EC.visibility_of(driver.find_element_by_css_selector(".item.next"))
                    )
                    next_page.click()
                    page_num +=1
                    time.sleep(10)
                except Exception as e:
                    print(e)
                    break
    def crawl(self,root_url,to_city):
        today = datetime.date.today().strftime('%Y-%m-%d')
        tomorrow = datetime.date.today()+datetime.timedelta(days=1)
        tomorrow = tomorrow.strftime('%Y-%m-%d')
        driver = webdriver.Firefox(executable_path='D:\Anaconda3\geckodriver.exe')
        driver.set_page_load_timeout(50)
        driver.get(root_url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        self.get_hotel(driver,to_city,today,tomorrow)

if __name__ == '__main__':
    spider = QunaSpider()
    spider.crawl('http://hotel.qunar.com/',u"太原")

class QunaSpider(object):
    def get_hotel(self,driver,to_city,fromdate,todate):
        ele_toCity = driver.find_element_by_name('toCity')
        ele_fromDate = driver.find_element_by_id('fromDate')
        ele_toDate = driver.find_element_by_id('toDate')
        ele_search = driver.find_element_by_class_name('search-btn')
        ele_toCity.clear()
        ele_toCity.send_keys(to_city)
        ele_toCity.click()
        ele_fromDate.clear()
        ele_fromDate.send_keys(fromdate)
        ele_toDate.clear()
        ele_toDate.send_keys(todate)
        ele_search.click()
        page_num = 0
        while True:
            try:
                WebDriverWait(driver,10).until(
                        EC.title_contains(str(to_city))
                        )
            except Exception as e:
                print (e)
                break
            time.sleep(5)
            js = "window.scrollTo(0, document.body.scrollHeight);"
            driver.execute_script(js)
            time.sleep(5)
            htm_const = driver.page_source
            soup = BeautifulSoup(htm_const,'html.parser',from_encoding='utf-8')
            infos = soup.find_all(class_="item_hotel_info")
            f = codecs.open(str(to_city)+str(fromdate)+u'.html','a+')
            for info in infos:
                f.write(str(page_num)+'--'*50)
                content = info.get_text().replace(" ","").replace("\t","").strip()
                for line in [ln for ln in content.splitlines()if ln.strip()]:
                    f.write(line)
                    f.write('\r\n')
                f.close()
                try:
                    next_page = WebDriverWait(driver,10).until(
                    EC.visibility_of(driver.find_element_by_css_selector(".item.next"))
                    )
                    next_page.click()
                    page_num +=1
                    time.sleep(10)
                except Exception as e:
                    print(e)
                    break



today = datetime.date.today().strftime('%Y-%m-%d')
tomorrow = datetime.date.today()+datetime.timedelta(days=1)
tomorrow = tomorrow.strftime('%Y-%m-%d')
driver = webdriver.Firefox()
driver.set_page_load_timeout(50)
driver.get('http://hotel.qunar.com/')
driver.maximize_window()
driver.implicitly_wait(10)

ele_toCity = driver.find_element_by_name('toCity')
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

from bs4 import BeautifulSoup
from lxml import html
import xml
import requests
import re
import pandas as pd
import time
import urllib.request
import urllib.parse

def get_soup(url):
	request =  urllib.request.Request(url=url,headers=headers)
	response = urllib.request.urlopen(request)
	response = response.read().decode()
	soup=BeautifulSoup(response, "lxml") 
	return soup

headers = {
	'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; 360SE)'
}

all_city = [
'https://hotels.ctrip.com/hotel/taiyuan105/p',
'https://hotels.ctrip.com/hotel/datong136/p',
'https://hotels.ctrip.com/hotel/shuozhou1317/p',
'https://hotels.ctrip.com/hotel/xinzhou513/p',
'https://hotels.ctrip.com/hotel/jinzhong1453/p',
'https://hotels.ctrip.com/hotel/yangquan907/p',
'https://hotels.ctrip.com/hotel/jincheng1092/p',
'https://hotels.ctrip.com/hotel/changzhi137/p',
'https://hotels.ctrip.com/hotel/lvliang7631/p',
'https://hotels.ctrip.com/hotel/yuncheng140/p',
'https://hotels.ctrip.com/hotel/linfen139/p'
]

df=pd.DataFrame()
for c in all_city:
	url = c + '1'
	soup=get_soup(url)
	total_hotel=soup.find("b",attrs={"id": "lblAmount"}).text
	page_amount=round(int(total_hotel)/25)
	for pg in range(1,page_amount):
		url=c+str(pg)
		print(c+'第'+str(pg)+'页')
		soup=get_soup(url)
		for a in soup.select("h2 > a"):
			hotel_href = 'https://hotels.ctrip.com'+ a['href']
			hotel_name = a['title']
			soup1 = get_soup(hotel_href)
			city=soup1.find("span",attrs={"id": "ctl00_MainContentPlaceHolder_commonHead_lnkCity"}).text
			location=soup1.find("span",attrs={"id": "ctl00_MainContentPlaceHolder_commonHead_lnkLocation"}).text
			address=soup1.find("span",attrs={"id": "ctl00_MainContentPlaceHolder_commonHead_lbAddress"}).text
			phone=soup1.find("span",attrs={"id": "J_realContact"})
			if phone != None:
				phone=re.sub(r'\xa0.*$',"",phone['data-real'])
			else:
				phone='暂无联系方式'
			print(hotel_name,city,location,address,phone)
			df=df.append([[hotel_name,city,location,address,phone]])
			time.sleep(5)
df.to_csv("ctrip_hotels.csv", encoding='utf_8_sig')


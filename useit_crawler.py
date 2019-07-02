# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
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

def get_soup(url):
 request =  urllib.request.Request(url=url,headers=headers)
 response = urllib.request.urlopen(request)
 response = response.read()#.decode('utf-8')
 soup=BeautifulSoup(response, "lxml") 
 return soup

headers = {
 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; 360SE)'
}

url0='https://www.useit.com.cn/forum-352-'
url='https://www.useit.com.cn/forum-352-1.html'
soup=get_soup(url)
page_amount=soup.find("span",attrs={"id": "fd_page_top"})
page_amount=re.sub(r'.*/ ',"",page_amount.text)
page_amount=re.sub(r' 页下一页',"",page_amount)
print(page_amount)
for page in range(1,int(page_amount)):
 page_url=url0+str(page)+'.html'
 print(page_url)
 soup=get_soup(page_url)
 content_list=soup.find_all("h3",attrs={"class": "xw0"})
 for content in content_list:
  content_title=re.sub(r'\n',"",content.text)
  print(content_title)
  content_url=content.find('a', href=True)['href']
  print(content_url)
  soup=get_soup(content_url)
  file_path='F:\\useit知识库'
  if not os.path.exists(file_path+'\\'+content_title):
   os.makedirs(file_path+'\\'+content_title)
  file_path=file_path+'\\'+content_title
  print(file_path)
  img_list=soup.find_all("img",attrs={'style':"cursor:pointer"})
  n=0
  for img in img_list:
   img_url=img['zoomfile']
   print(img_url)
   #response = requests.get(img_url)
   #img_data = response.content
   request =  urllib.request.Request(url=img_url,headers=headers)
   print("Request OK!")
   response = urllib.request.urlopen(request)
   print("reponse OK!")
   img_data = response.read()
   print("image download OK!")
   with open(file_path+'\\'+str(n)+'.jpg', 'wb') as f:
    f.write(img_data)
   print("image write OK!")
   print(file_path+'\\'+str(n))
   n=n+1
   time.sleep(5)
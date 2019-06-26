1、http://api.map.baidu.com/place/v2/search?q=酒店&region=大同市&page_size=10&page_num=0&output=json&ak=ONzSMFNjStddVEbVfLLfPanEC6YYGi7L
2、http://api.map.baidu.com/place/v2/detail?uid=34e485088952dbfbd8d89105&output=json&scope=2&ak=ONzSMFNjStddVEbVfLLfPanEC6YYGi7L
3、http://api.map.baidu.com/place/v2/search?query=酒店&page_size=10&page_num=0&scope=1&bounds=39.915,116.404,39.975,116.414&output=json&ak=ONzSMFNjStddVEbVfLLfPanEC6YYGi7L

eikVTDrvMvVnPldFlh44DWdUAKpq1xfL
import requests
def get_soup(url):
 page=requests.get(url)
 soup=BeautifulSoup(page.content, "lxml") 
 return soup

# -*- coding: utf-8 -*-

import time
import json
import pandas as pd
import requests
from pandas.io.json import json_normalize


left_bottom = [110.3296320000,34.5518820000]; # 设置区域左下角坐标（百度坐标系）
right_top = [114.5426130000,40.4742700000]; # 设置区域右上角坐标（百度坐标系）
part_n = 3; # 设置区域网格（3*3）

url0 = 'http://api.map.baidu.com/place/v2/search?'
x_item = (right_top[0]-left_bottom[0])/part_n
y_item = (right_top[1]-left_bottom[1])/part_n
query = '酒店'; #搜索关键词设置
ak = 'ONzSMFNjStddVEbVfLLfPanEC6YYGi7L' #百度地图api信令
n = 0; # 切片计数器

hotel_list=pd.DataFrame()
url='http://api.map.baidu.com/place/v2/search?q=宾馆&region=太原&output=json&ak=ONzSMFNjStddVEbVfLLfPanEC6YYGi7L'
r = requests.get(url)
hotels = json.loads(r.text)['results']
for h in hotels:
 uid=h['uid']
 url0='http://api.map.baidu.com/place/v2/detail?uid='
 url1='&output=json&scope=2&ak=ONzSMFNjStddVEbVfLLfPanEC6YYGi7L'
 url=url0+uid+url1
 r1 = requests.get(url)
 hotel_detail=json.loads(r1.text)['result']
 df = json_normalize(hotel_detail)
 hotel_list=hotel_list.append(df)
hotel_list.to_csv('hotel_list.csv',encoding='utf_8_sig')

for i in range(1):
 for j in range(1):
  left_bottom_part = [left_bottom[0]+i*x_item,left_bottom[1]+j*y_item]; # 切片的左下角坐标
  right_top_part = [right_top[0]+i*x_item,right_top[1]+j*y_item]; # 切片的右上角坐标
  for k in range(20):
   url = url0 + 'query=' + query + '&page_size=20&page_num=' + str(k) + '&scope=1&bounds=' + str(left_bottom_part[1]) + ',' + str(left_bottom_part[0]) + ','+str(right_top_part[1]) + ',' + str(right_top_part[0]) + '&output=json&ak=' + ak
   r = requests.get(url)
   hotels = json.loads(r.text)['results']
   for h in hotels:
    uid=h['uid']
    url0='http://api.map.baidu.com/place/v2/detail?uid='
    url1='&output=json&scope=2&ak=ONzSMFNjStddVEbVfLLfPanEC6YYGi7L'
    url=url0+uid+url1
    r1 = requests.get(url)
    hotel_detail=json.loads(r1.text)['result']
    df = json_normalize(hotel_detail)
    hotel_list=hotel_list.append(df)
   n += 1;
   print ('第',str(n),'个切片入库成功')


df = pd.DataFrame()
for i in range(2):
 for j in range(part_n):
  left_bottom_part = [left_bottom[0]+i*x_item,left_bottom[1]+j*y_item]; # 切片的左下角坐标
  right_top_part = [left_bottom[0]+(i+1)*x_item,left_bottom[1]+(j+1)*y_item]; # 切片的右上角坐标
  str(left_bottom_part[1]) + ',' + str(left_bottom_part[0]) + ','+str(right_top_part[1]) + ',' + str(right_top_part[0])
  for k in range(20):
   url = url0 + 'query=' + query + '&page_size=20&page_num=' + str(k) + '&bounds=' + str(left_bottom_part[1]) + ',' + str(left_bottom_part[0]) + ','+str(right_top_part[1]) + ',' + str(right_top_part[0]) + '&output=json&ak=' + ak
   time.sleep(10)
   r = requests.get(url)
   hotels = json.loads(r.text)['results']
   for h in hotels:
    uid=h['uid']
    hotel_name=h['name']
    address=h['address']
    province=h['province']
    city=h['city']
    area=h['area']
    if h.__contains__('telephone'):
     telephone=h['telephone']
    else:
     telephone=' '
    df=df.append([[uid,hotel_name,address,province,city,area,telephone]])
df.to_csv("hospital_list.csv",  encoding='utf_8_sig')
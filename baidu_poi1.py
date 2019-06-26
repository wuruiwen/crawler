太原市小店区,112.377499,37.603169,112.795902,37.968142
太原市迎泽区,112.530291,37.803189,112.744295,37.853869
大同市平城区,113.129651,39.987201,113.454478,40.182837
大同市云冈区,112.835275,39.859842,113.496428,40.190463
大同市云州区,113.485666,39.755521,114.049083,40.498727
阳泉市城区,113.536429,37.840441,113.657162,37.912446
阳泉市矿区,113.48678,37.854581,113.48678,37.854581
阳泉市郊区,113.22231,37.768019,113.740883,38.145855
晋城市城区,112.639391,35.380481,113.093575,35.701904
晋城市阳城县,111.976467,35.188084,112.684763,35.708417
晋中市平遥县,111.196397,35.312488,112.535456,37.381874
运城市盐湖区,110.708868,34.811392,111.196397,35.312488

运城市空港新区,111.037787,35.092203,111.079468,35.126161

忻州市五台县,112.98089,38.584289,113.750127,39.107637
临汾市尧都区,111.298974,35.916609,111.87044,36.261003
长治市潞州区,112.971994,36.121593,113.246804,36.454167

长治市上党区,112.92691,35.89502,113.20057,36.117385
长治市屯留区,112.504079,36.073948,112.997356,36.548575
长治市潞城区,113.027459,36.218889,113.418401,36.543391

39.755521,113.485666,40.498727,114.049083
37.840441,113.536429,37.912446,113.657162
37.768019,113.22231,38.145855,113.740883
35.380481,112.639391,35.701904,113.093575
35.092203,111.037787,35.126161,111.079468
35.89502,112.92691,36.117385,113.20057
36.073948,112.504079,36.548575,112.997356
36.218889,113.027459,36.543391,113.418401

import time
import json
import pandas as pd
import requests
import math


hot_area=[
[37.603169,112.377499,37.968142,112.795902],
[37.803189,112.530291,37.853869,112.744295],
[39.987201,113.129651,40.182837,113.454478],
[39.859842,112.835275,40.190463,113.496428],
[35.188084,111.976467,35.708417,112.684763],
[35.312488,111.196397,37.381874,112.535456],
[34.811392,110.708868,35.312488,111.196397],
[38.584289,112.98089,39.107637,113.750127],
[35.916609,111.298974,36.261003,111.87044],
[36.121593,112.971994,36.454167,113.246804]
]

hot_area=[
[37.656772,112.214321,38.158539,112.86915]
]


hot_area=[
[37.603169,112.377499,37.968142,112.795902],
[37.803189,112.530291,37.853869,112.744295]
]

part_n = 8; # 设置区域网格（3*3）

query = '酒店'; #搜索关键词设置
url0 = 'http://api.map.baidu.com/place/v2/search?' + 'query=' + query + '&page_size=20&page_num='
ak = 'ONzSMFNjStddVEbVfLLfPanEC6YYGi7L' #百度地图api信令
url1 = '&output=json&ak=' + ak

df = pd.DataFrame()
for h_area in hot_area:
	left_bottom = [h_area[1],h_area[0]]
	right_top = [h_area[3],h_area[2]]
	x_item = (right_top[0]-left_bottom[0])/part_n
	y_item = (right_top[1]-left_bottom[1])/part_n 
	for i in range(part_n):
		for j in range(part_n):
			left_bottom_part = [left_bottom[0]+i*x_item,left_bottom[1]+j*y_item]; # 切片的左下角坐标
			right_top_part = [left_bottom[0]+(i+1)*x_item,left_bottom[1]+(j+1)*y_item]; # 切片的右上角坐标
			location = str(left_bottom_part[1]) + ',' + str(left_bottom_part[0]) + ','+str(right_top_part[1]) + ',' + str(right_top_part[0])
			time.sleep(10)
			url = url0 + '0' + '&bounds=' + location + url1
			r = requests.get(url)
			total = json.loads(r.text)['total']
			t = math.ceil(total/20)
			print(total,t)
			for k in range(t):
				if k == 0:
					hotels = json.loads(r.text)['results']
				else:
					time.sleep(10)
					url = url0 + str(k) + '&bounds=' + location + url1
					print(url)
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
					print(hotel_name,address,telephone)

df.to_csv("hotels_list3.csv",  encoding='utf_8_sig')

# -*- coding: utf-8 -*-

import requests
from lxml import etree
import datetime

#url = "http://icp.chinaz.com/provinces?&companytype=&city=%u5C71%u897F&custype=0&companyName=&page=1"
#url='http://icp.chinaz.com/provinces/%E5%B1%B1%E8%A5%BF/7'
url="http://icp.chinaz.com/provinces?&time=7&companytype=&city=%u5C71%u897F&custype=0&companyName=&page=3"
#headers = {
#	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
#	'Connection': 'keep-alive',
#	'Host': 'icp.chinaz.com',
#	'Cookie': 'UM_distinctid=16b408a0349665-03100f046722f2-6b1b1279-140000-16b408a034a620; qHistory=cHJvdmluY2VzLyvmnIDmlrDlpIfmoYjln5/lkI0v6auY57qn5p+l6K+ifGZpbmQvK+aJvuWbnuWkh+ahiOWvhueggXxyZWNvcmQvK+Wfn+WQjeWkh+ahiOiusOW9lXxodHRwOi8vaWNwLmNoaW5hei5jb20vK+e9keermeWkh+ahiHxodHRwOi8vdG9vbC5jaGluYXouY29tX+ermemVv+W3peWFtw==',
    #'Cookie': 'UM_distinctid=16b408a0349665-03100f046722f2-6b1b1279-140000-16b408a034a620; avatarId=5dc3c18d-0f3b-4c19-ae31-2d98f4d1cd46-; ASP.NET_SessionId=3iub1lqsekjspyys2zsey0uw; rh=xz.beian.miit.gov.cn; rc=JSESSIONID=BAE7386BC06B44EDA5ACE4CBD2E8FE97; qHistory=cHJvdmluY2VzLyvmnIDmlrDlpIfmoYjln5/lkI0v6auY57qn5p+l6K+ifGZpbmQvK+aJvuWbnuWkh+ahiOWvhueggXxyZWNvcmQvK+Wfn+WQjeWkh+ahiOiusOW9lXxodHRwOi8vaWNwLmNoaW5hei5jb20vK+e9keermeWkh+ahiHxodHRwOi8vdG9vbC5jaGluYXouY29tX+ermemVv+W3peWFtw==; CNZZDATA5082706=cnzz_eid%3D464815940-1560295100-null%26ntime%3D1561451161',
#	'Accept': 'zh-CN,zh;q=0.8',
#	'Referer': 'http://icp.chinaz.com/provinces/%E5%B1%B1%E8%A5%BF/7'
#	}

headers = {
    'Host': 'icp.chinaz.com',
    'Connection': 'keep-alive',
    #'Content-Length': '92',
    #'Cache-Control': 'max-age=0',
    #'Origin': 'http://icp.chinaz.com',
    #'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://icp.chinaz.com/provinces?&time=7&companytype=&city=%u5C71%u897F&custype=0&companyName=&page=2',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cookie': 'UM_distinctid=16b408a0349665-03100f046722f2-6b1b1279-140000-16b408a034a620; avatarId=5dc3c18d-0f3b-4c19-ae31-2d98f4d1cd46-; ASP.NET_SessionId=3iub1lqsekjspyys2zsey0uw; rh=xz.beian.miit.gov.cn; rc=JSESSIONID=BAE7386BC06B44EDA5ACE4CBD2E8FE97; qHistory=cHJvdmluY2VzLyvmnIDmlrDlpIfmoYjln5/lkI0v6auY57qn5p+l6K+ifGZpbmQvK+aJvuWbnuWkh+ahiOWvhueggXxyZWNvcmQvK+Wfn+WQjeWkh+ahiOiusOW9lXxodHRwOi8vaWNwLmNoaW5hei5jb20vK+e9keermeWkh+ahiHxodHRwOi8vdG9vbC5jaGluYXouY29tX+ermemVv+W3peWFtw==; CNZZDATA5082706=cnzz_eid%3D464815940-1560295100-null%26ntime%3D1561508688',
    }

response = requests.get(url, headers=headers,timeout=60)
content = response.content.decode('utf-8')

print(url)
print(headers)
print(content)

html = etree.HTML(content)

domain_list = html.xpath('//tbody[@id="result_table"]//tr/td[1]/a/@title')
print(domain_list)
organizer_list = html.xpath('//tbody[@id="result_table"]//tr/td[2]/text()')
print(organizer_list)
nature_list = html.xpath('//tbody[@id="result_table"]//tr/td[3]/text()')
print(nature_list)
license_list = html.xpath('//tbody[@id="result_table"]//tr/td[4]/text()')
print(license_list)
web_name_list = html.xpath('//tbody[@id="result_table"]//tr/td[5]/text()')
print(web_name_list)
verify_time_list = html.xpath('//tbody[@id="result_table"]//tr/td[7]/text()')
print(verify_time_list)
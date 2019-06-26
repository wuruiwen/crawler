# -*- coding: utf-8 -*-

import requests
from lxml import etree
import datetime

uri = "http://icp.chinaz.com/provinces?prov=%e5%85%a8&domain=10&page="

def get_today():
    today = datetime.datetime.now()
    today = today.strftime("%Y-%m-%d")
    return today


def url_open(url):
    page_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
        'Connection': 'keep-alive',
        'Host': 'icp.chinaz.com',
        'Cookie': 'UM_distinctid=162903806a7d3d-04634c5630b967-4d015463-1fa400-162903806a8507; qHistory=aHR0cDovL2ljcC5jaGluYXouY29tLyvnvZHnq5nlpIfmoYh8cHNvcmdhbi8r572R5a6J5aSH5qGIfHNlYXJjaHMvK+aJuemHj+afpeivonxodHRwOi8vd2hvaXMuY2hpbmF6LmNvbS8rV2hvaXPmn6Xor6J8Y29uZGl0aW9ucy8r5aSH5qGI5Z+f5ZCN6auY57qn5p+l6K+i; CNZZDATA5082706=cnzz_eid%3D1585686909-1526612935-null%26ntime%3D1526629135; rip=tVNjEkQ|MkLE453hZldn3g==; rh=ki7P5D8g5j8Wl6yMNM2WAU/yxWtIIg20gIg7pBclWnY=; rc=|MclsOz|7oxw7gkzdKh7gCi4mO2OkWvzqEfgrZjM77eS2uJ8/RWO4HQLXwr4euUFNdOe9EMWMOAl3IrQlldthI7E0SfJKlz75AIcRrgpl1moKutX3ZHJtw==',
        'Accept': 'zh-CN,zh;q=0.8',
        'Referer': 'http://icp.chinaz.com/'
    }

    try:
        res = requests.get(url, headers=page_headers,timeout=60)
        status = res.status_code
        # print(status)
        content = res.content.decode('utf-8')
        return status, content
    except Exception as e:
        print(str(e))
        return 0, 0


def get_record_domain():
    today = get_today()
    j = 1
    while j != 0:
        url = uri + str(j)
        print(url)
        status, content = url_open(url)
        if status == 200:
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

            num = len(domain_list)
            for i in range(num):
                domain = domain_list[i].replace('http://', '').replace('https://', '')
                organizer = organizer_list[i]
                nature = nature_list[i]
                licenseN = license_list[i]
                web_name = web_name_list[i]
                verify_time = verify_time_list[i]
                if verify_time == today:
                    # print(domain + "\n" + organizer + "\n" + nature + "\n" + licenseN + "\n" + web_name + "\n" + verify_time + "\n")
                    with open('record_domain.csv', 'a+', encoding='utf-8') as fh:
                        fh.write(domain + "," + organizer + "," + nature + "," + licenseN + "," + web_name + "," + verify_time + "\n")

            continue_flag = verify_time_list[num - 1]
            if continue_flag == today:
                j += 1
            else:
                break

get_record_domain()


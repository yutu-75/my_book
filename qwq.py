# coding: utf-8

import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Cookie': 'Hm_lvt_40639e2e855ad00c65304ee021f07859=1619532565,1619573478; Hm_lpvt_40639e2e855ad00c65304ee021f07859=1619573815',
}



# page = requests.get(url='https://www.ddxstxt8.com/5_2082/',headers=headers)
# page.encoding = 'GBK'
# page_text = page.text
# print(page_text)

url_z = 'https://www.ddxstxt8.com/5_2082/44219013.html'

page = requests.get(url=url_z,headers=headers)
page.encoding = 'GBK'
page_text = page.text
print(page_text)







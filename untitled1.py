# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:49:28 2018

@author: lenovo
"""

import urllib.request as r

url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'

info=r.urlopen(url.format('zhengzhou')).read().decode('utf-8','ignore')

import json

data=json.loads(info)



for j in range(0,5):
    print('第'+str(j+1)+'天天气状况')
    for i in range(0,7):
        print('时间：'+data['list'][i+j*8]['dt_txt']+'\t')
        print('最高气温~最低温度：'+str(data['list'][i+j*8]['main']['temp_max'])+'开式度'+'~'+str(data['list'][i+j*8]['main']['temp_max'])+'开式度'+'\t')
        print('实时温度：'+str(data['list'][i+j*8]['main']['temp'])+'开式度'+'\t')
        print('气压：'+str(data['list'][i+j*8]['main']['pressure'])+'帕'+'\t')
        print('天气状况：'+data['list'][i+j*8]['weather'][0]['description']+'\t')
        print('湿度：'+str(data['list'][i+j*8]['main']['humidity'])+'\t')
        print('\t'*2)
    print('*'*100)


















import time
print('欢')

time.sleep(3)

print('迎')
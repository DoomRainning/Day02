# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 17:19:08 2018

@author: lenovo
"""

import urllib.request as r
import json
import time
#欢迎界面
print('欢迎使用城市天气查询系统')
time.sleep(1)
a=input('尊敬的使用者，您是第一次使用本系统吗？ 请输入：YES  or  NO ')
#判断选择
if a==YES:
    time.sleep(1)
    print('欢迎第一次使用天气查询系统')
    time.sleep(1)
    z=input('菜单是：1.查看当前城市天气   2.查看其它城市天气  ')
else：
    time.sleep(1)
    z=input('菜单是：1.查看当前城市天气   2.查看其它城市天气  ')
#城市查询
    #城市名字确定
if z==1:
    city='leshan'
else:
    city=input('请输入城市拼音：')
    
city_address="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996 ".format(city)
info=r.urlopen(city_address).read().decode('utf-8','ignore')

    #城市天气信息展示
data=json.loads(info)
index=int(len(data['list']))

information_weather=[]

for i in range(0,index):
    day=data['list'][i]
    time=day['dt_txt']
    temp=day['main']['temp']
    description=day['weather'][0]['description']
    temp_max=day['main']['temp_max']
    pressure=day['main']['pressure']
    information_weather=('{} 当前时间{}温度为{}，天气情况{}，最高温度{}，气压为{}'.format(city,time,temp,description,temp_max,pressure))
    print(information_weather)

#信息存储




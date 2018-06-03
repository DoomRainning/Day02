# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:42:37 2018

@author: lenovo
"""
#一次申请一个变量
a=3

#一次申请多个变量

xuan,guibin,xixi=80,90,88
xj="小娇"
yanzhi=5.4444444444

#自动补全代码 按 Tab
#TypeError:must be str not float
print(xj+yanzhi)
#将其他类型转换成字符串类型
b=str(yanzhi)
c='3.9'
d=float(c)



print(xj+str(yanzhi))
#字符串中出现{}大括号，表示占位符
print('今天温度是{}天气是{}今天星期{}'.format(10,'晴','六'))

#列表list，加中括号为list 不加为 tuple
usemoney=12,20,30,19,20
usemoney[1]
usemoney[0]
usemoney2=[12,20,30,19,20]
print(usemoney2[0])




day=["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
print(day[0])
print(day[1])
print(day[2])
print(day[3])
print(day[4])
print("今天是{}".format(day[5]))
print(day[6])





'''
字典练习
{
"地址"："你猜我的地址在哪里呀"
"手机号":"就不告诉你我的手机号"
"寄信人":"有谁会给你寄信心里没点笔数吗"
}
'''

msq={"地址":"你猜我的地址在哪里呀",
"手机号":"就不告诉你我的手机号",
"寄信人":"有谁会给你寄信心里没点笔数吗"}

print(msq["地址"])

print(msq["手机号"])

print(msq["寄信人"])





Private_information={'姓名':'你二大爷',
                     '年龄':'不肖子孙啊，连你二大爷多少岁都不知道了',
                     '性别':'你滚，从此我们恩断义绝',
                     '身高':'总是比你高那么一丢丢',
                     '体重':[150,162,1,5648,52648,456],
                     '爱好':['吃西瓜','读书','练字','品尝美食']}
x=Private_information["体重"]

y=Private_information['爱好']

print(x)

print(len(x))

print('爱好种类数量'+str(len(y)))

print(max(y))





'''
第一次
'''

weather={'时间':['6-2','6-3','6-4','6-5','6-6'],
        '温度':['20~27','18~24','18~28','19~30','22~31'],
        'temp':[23,27,24,21,21],
        '星期':(6,7,1,2,3),
        }

print('未来5天的最高温度是：{}'.format(max(weather['temp'])))





city_pinyin=input('请输入城市拼音：')
print(city)

address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
print(address.format(city_pinyin))
#1.查看当前城市天气 2.查看其它城市天气 3.保存当前城市天气

print('1.查看当前城市天气 2.查看其它城市天气 3.保存当前城市天气')
menno=input('请输入菜单序列号（1 or 2 or 3）：')

if menno=='1':
    print("1.查看当前城市天气")

if menno=='1':
    print("2.查看其它城市天气 ")
    
if menno=='1':
    print("3.保存当前城市天气")
    
    


import urllib.request as r  #url 网上资源地址

city_pinyin=input('请输入城市拼音：')

address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'

#网络连接
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')

print(info)   #此时info的格式是字符串形式  我们需要将它转换成地点形式

#json(dict)  格式工具包

import json
data=json.loads(info)  #转换为字典形式

data['main']['temp']

y=data['main']['pressure']

data['main']['humidity']

data['main']['temp_min']

x=data['main']['temp_max']

z=data['weather'][0]['main']
print('查看当前城市天气')
print('当前城市最高温度：'+'\t'+str(x))
print('当前城市气压：'+'\t'+str(y))
print('当前城市天气状况：'+'\t'+str(z))

#实际操作
import urllib.request as r
import json
print('郑州未来7天的天气状况')
address='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address).read().decode('utf-8','ignore')
data=json.loads(info)
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:49:28 2018

@author: lenovo
"""

import urllib.request as r

url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'

info=r.urlopen(url.format('tianjin')).read().decode('utf-8','ignore')

import json

data=json.loads(info)

data['list'][1]['weather'][0]['description']
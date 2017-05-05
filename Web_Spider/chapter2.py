#!/usr/bin/python
#coding=utf-8
'''
Created on 2016年4月25日

@author: wujianxin
'''

import urllib.request

keyword = {}
keyword['word'] = '汽车之家'

'将dict转换可拼接为url字符串的形式'
url_values = urllib.parse.urlencode(keyword)
url = 'http://www.baidu.com/s?'
full_url = url + url_values
print(full_url)

data = urllib.request.urlopen(url).read()
data = data.decode('utf-8')
print(data)

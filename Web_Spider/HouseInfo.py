#!/usr/bin/python
#coding=utf-8
'''
Created on 2016年4月25日

@author: wujianxin
'''

#coding=utf-8
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

url='http://chengde.58.com/cdkaifaqu/ershoufang/'

district='开发区'

html = getHtml(url)
# house_info = open('./house_info.txt', 'w')
# house_info.write(html.decode('utf-8'))
# house_info.close()
print(html.decode('utf-8'))
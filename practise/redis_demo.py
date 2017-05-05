#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: wujianxin
'''
import redis

if __name__ == '__main__':
    r=redis.StrictRedis(host='192.168.1.7',port=6379,db=0)
    r.get('1_442162')
    print(r.get('1_442162'))
    pass
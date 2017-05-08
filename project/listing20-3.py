#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: wujianxin
'''
import sys, re
from util import *

src = './listing20-1.txt'
target = './listing20-1.html'
f = open(target,'w')
f.write('<html><head><title>...</title><body>')

title = True
for block in blocks(open(src)):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        f.write('<h1>')
        f.write(block)
        f.write('</h1>')
        title = False
    else:
        f.write('<p>')
        f.write(block)
        f.write('</p>')

f.write('</body></html>')
f.close()
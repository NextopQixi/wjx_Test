#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: wujianxin
'''
def lines(file):
    for line in file: 
        yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
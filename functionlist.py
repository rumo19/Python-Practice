# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 03:33:07 2018

@author: Hasan
"""

def chop(a):
    del a[0]
    del a[-1]
b=[1,2,3,4]
chop(b)
print(b)


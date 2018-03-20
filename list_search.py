# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 02:44:20 2018

@author: Hasan
"""

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])
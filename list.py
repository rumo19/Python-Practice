# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 00:56:22 2018

@author: Hasan
"""

newlist=list()
while True:
    input_number=input('Enter a Number: ')
    if input_number=='done':
        break
    float_value=float(input_number)
    newlist.append(float_value)

average1 =sum(newlist)/len(newlist)
print('Avearge: ', average1)

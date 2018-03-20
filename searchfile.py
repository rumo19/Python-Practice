# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 04:18:01 2018
Rewrite the guardian code in the above example without
 two if statements. Instead, use a compound logical 
 expression using the and logical operator with a single if statement.
@author: Hasan
"""




fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:',words)
    if len(words) == 0 or words[0] != 'From' : continue
   
    print(words[2])
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 20:00:21 2018

@author: Hasan
"""
"""
random number
import random
for i in range (10):
    x=random.random()
    print (x) 
    
    """
    #choice function
import random
"""
t = [1, 2, 3]
print (random.choice(t))

from math import*

signal_power=10
noise_power=5
ratio = signal_power / noise_power
decibels = 10 * log10(ratio)
print (decibels)
radians = 0.7
height = sin(radians)
print(height)
degrees = 45
radians = degrees / 360.0 * 2 * pi
print (sin(radians))

def print_lyrics():
     print("I'm a lumberjack, and I'm okay.")
     print('I sleep all night and I work all day.')
def repeat_function():
    print_lyrics()
    print_lyrics()
    #Loop

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

#count the total number of a set and max 
count=0
max1=None
for i in [10,10,11,12,13,14]:
    if(max1 is None or i>max1):
       max1=i
    count=count+1
print (count, max1)

sum=0
a=0
while True:
    a=input('Enter a number :')
    if (a=='Done'):
        break
    else:
        sum=sum+ int(a)
        
print(sum)

while True:
    line = input('><<<<< ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

### file 


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    print(line.upper())
    """
fhand = open('mbox-short.txt')
sum=0
count=0
for line in fhand:
    
    if line.find('X-DSPAM-Confidence:') == -1: 
        continue
    a=line.find('X-DSPAM-Confidence:')
    
    b=line.find(' ',a)
    d=line.find(' ',b+1)
    c=line[b:d]
    sum=sum+float(c)
    count=count+1
avgg=sum/count
print (avgg)
    
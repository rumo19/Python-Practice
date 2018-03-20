# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 09:32:59 2018
7.2 Write a program that prompts for a file name,
 then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point 
values from each of the lines and compute the 
average of those values and produce an output
 as shown below. Do not use the sum() function 
 or a variable named sum in your solution.
You can download the sample data at 
http://www.py4e.com/code3/mbox-short.txt when
 you are testing below enter mbox-short.txt as the file name.
@author: Hasan
"""



total=0
count=0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    a=line.find(':')
    #b=line.find(' ',a+1) #a start upto ''
    newtext=line[a+1:]
    print(newtext)
    newtexttofloat=float(newtext)
    total=total+newtexttofloat
    count=count+1
        
    
print("Average spam confidence:",total/count)
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 09:49:27 2018
8.4 Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split() method. 
The program should build a list of words. For each word on e
ach line check to see if the word is already in the list and 
if not append it to the list. When the program completes, sort and 
print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
@author: Hasan
"""


fopenf=open("romeo.txt", "r")

new_list=[]
new_wordlist=[]
for line in fopenf:
    new_list=line.split()
    for word in new_list:
        if word in new_wordlist:
            continue
        new_wordlist.append(word)




sortlist=sorted(new_wordlist)

print(sortlist)

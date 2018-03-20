# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 04:42:01 2018
Write a program to open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split function.

For each word, check to see if the word is already in a list. 
If the word is not in the list, add it to the list.

When the program completes, sort and print the resulting words in alphabetical order.
@author: Hasan
"""

fopenf=open('romeo.txt','r')
print(fopenf)
new_list=[]
new_wordlist=[]
for line in fopenf:
    new_list=line.split()
    for word in new_list:
        new_wordlist.append(word)



new_word=input('Enter a new word : ')
if new_word in new_wordlist:
    print('The word already exit')
else:
    new_wordlist.append(new_word)
sortlist=sorted(new_wordlist)
print(sortlist)


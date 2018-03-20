# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 05:47:02 2018
Exercise 6: Rewrite the program 
that prompts the user for a list 
of numbers and prints out the maximum and
 minimum of the numbers at the end when
 the user enters "done". Write the program 
 to store the numbers the user enters in a 
 list and use the max()
 and min() functions to compute 
 the maximum and minimum numbers 
 after the loop completes.
@author: Hasan
"""
newlist=list()
while True:
    input_number=input('Enter a Number: ')
    if input_number=='done':
        break
    
    newlist.append(int (input_number))
print(newlist)
print (max(newlist))
print (min(newlist))
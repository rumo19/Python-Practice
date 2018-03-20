# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 07:51:15 2018
5.2 Write a program that repeatedly
 prompts a user for integer numbers 
 until the user enters 'done'.
 Once 'done' is entered, 
 print out the largest and
 smallest of the numbers. 
 If the user enters anything 
 other than a valid number catch it with a try/except 
and put out an appropriate 
message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
@author: Hasan
"""

largest = None
smallest = None
flag=0
while True:
    try:
       num = input("Enter a number:")
       if num =="done" : 
        break
       num=int(num)
       
    except ValueError:
        flag=1
        continue
    
    if largest is None or largest<num:
        largest=num
    if smallest is None or smallest>num:
        smallest=num
    
if flag==1:
    print("Invalid input")
print("Maximum is", largest)
print("Minimum is", smallest)
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 06:48:47 2018
3.1 Write a program to prompt the user 
for hours and rate per hour using input to 
compute gross pay. Pay the hourly rate for the 
hours up to 40 and 1.5 times the hourly rate for all
 hours worked above 40 hours. Use 45 hours and a rate of 
 10.50 per hour to test the program (the pay should be 498.75).
 You should use input to read a string and float() to convert the 
 string to a number. 
Do not worry about error checking the user input - assume the user types numbers properly.
@author: Hasan
"""

hours = input("Enter Hours:")
hours=float(hours)

rate=input("Enter rate:")
rate=float(rate)
if hours>40:
    rate=1.5*rate
    grosspay=40*10.50+rate*(hours-40)
else:
    grosspay=hours*rate
print('Pay:',grosspay)
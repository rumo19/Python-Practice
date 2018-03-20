# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 09:03:43 2018
6.5 Write code using find() and string
 slicing (see section 6.10) to extract the number at the end of
 the line below. Convert the extracted 
 value to a floating point number and print it out.
@author: Hasan
"""

text = "X-DSPAM-Confidence:    0.8475"
b=text.find(':')
new_text=text[b+1:]
print(float(new_text))

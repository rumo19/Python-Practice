import re
import os
fileDir = os.path.dirname(os.path.realpath('mbox-short.txt'))
print (fileDir)

#For accessing the file in the parent folder of the current folder
filename = os.path.join(fileDir, '../mbox-short.txt')


fileopen=open(filename)
for line in fileopen:
    line=line.rstrip()
    #if re.search('^From',line): #check beginning of line 
    #if re.search('^F..m',line):  #F..m:" would match any of the strings "From:", "Fxxm:", "F12m:", or "F!@m:"# Search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'This is particularly powerful when combined with the ability to indicate that a character can be repeated any number of times using the "*" or "+" characters in your regular expression. These special characters mean that instead of matching a single character in the search string, they match zero-or-more characters (in the case of the asterisk) or one-or-more of the characters (in the case of the plus sign).
    # Search for lines that start with From and have an at sign
   
    ##if re.search('^From:.*@',line):
        #print(line)
        # Search for lines that have an at sign between characters
# The characters must be a letter or number
    line = line.rstrip()
    lst = re.findall('^X\S*: ([0-9.]+)', line)
    #if len(lst)>0:
        #print(lst)
    # Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
     
   ## if re.search('^X\S*: [0-9.]+', line):
   # Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a space
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.
    if len(lst)>0:
        print(lst) 
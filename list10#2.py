"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

Author: Hasan

"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hour=dict()
for line in handle:
    line1=line.split()
    if len(line1)>5 and line1[0]=="From":
        line2=line1[5].split(':')
        hour[line2[0]]=hour.get(line2[0],0)+1
hour=list(hour.items())
hour.sort()
for k,v in hour:
    print (k,v)
        

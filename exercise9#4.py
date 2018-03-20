"""
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""




name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
newdic=dict()
for line in handle:
    listline=line.split()
    if len(listline)<1 or listline[0] is not "From":
        continue
    
    newdic[listline[1]]=newdic.get(listline[1], 0)+1
    lst=list(newdic.values())
    maxvalue=max(lst)
for values in newdic:
    if newdic[values]==maxvalue:
       print(values, maxvalue)
       break
        
        
        
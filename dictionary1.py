word='brontosauurus'
d=dict()
for c in word:
    if c not in d :
        d[c]=1
    else:
        d[c]=d[c]+1
print(d)
#get method
for key in word:
    d[key]=d.get(key,0)+1
print(d)
#counting word from file
filef=input("Enter a file name ")
try:
    fileopen=open(filef)
except:
    print("File is not exit")
    exit()
count=dict()
for line in fileopen:
    words=line.split()
    for word in words:
        count[word]=count.get(word,0)+1
#print(count)
#loop in dictionaries
for key in count:
    if count[key]>1:
        print(key,count[key])
#keys in alphabetical order

lst=list(count.keys())
print(lst)
lst.sort()
for word in lst:
    print(word,count[word])


